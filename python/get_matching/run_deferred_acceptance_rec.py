from tco import with_continuations
from python.get_matching.libs.admint_next_application import (
    admit_next_application,
)
from python.get_matching.libs.get_admitted_applicant import get_admitted_applicant
from python.get_matching.libs.get_marginal_admitted_applicant import (
    get_marginal_admitted_applicant,
)
from python.get_matching.libs.get_next_application import (
    get_next_application,
)
from python.get_matching.libs.get_next_proposer import get_next_proposer
from python.get_matching.libs.has_marginal_applicant import (
    is_contract_full,
)
from python.get_matching.libs.has_proposer import has_proposer
from python.get_matching.libs.add_admitted_applicant_to_contract import (
    add_admitted_applicant_to_contract,
)
from python.get_matching.libs.reject_current_application import (
    reject_current_application,
)
from python.get_matching.libs.reject_next_application import (
    reject_next_application,
)
from python.get_matching.libs.remove_admitted_applicant_from_contract import (
    remove_admitted_applicant_from_contract,
)
from python.get_matching.libs.update_applicants import update_applicants
from python.types import Applicants, Contracts, AdmittedApplicant


@with_continuations()
def run_deferred_acceptance_rec(
    applicants: Applicants, contracts: Contracts, self=None
) -> Applicants:
    if not has_proposer(applicants=applicants):
        return applicants

    proposer = get_next_proposer(applicants=applicants)
    application = get_next_application(applicant=proposer)
    proposed_contract = contracts[application.contract]
    if proposed_contract.capacity == 0:
        return self(
            update_applicants(
                applicants=applicants,
                applicant=reject_next_application(applicant=proposer),
            ),
            contracts,
        )
    if not is_contract_full(contract=proposed_contract):
        contract_with_new_applicant = add_admitted_applicant_to_contract(
            applicant=AdmittedApplicant(
                applicant_id=proposer.id, priority_score=application.priority_score
            ),
            contract=proposed_contract,
        )
        return self(
            update_applicants(
                applicants=applicants,
                applicant=admit_next_application(applicant=proposer),
            ),
            {
                **contracts,
                contract_with_new_applicant.id: contract_with_new_applicant,
            },
        )
    else:
        marginal_applicant = get_marginal_admitted_applicant(contract=proposed_contract)
        if marginal_applicant.priority_score > application.priority_score:
            return self(
                update_applicants(
                    applicants=applicants,
                    applicant=reject_next_application(applicant=proposer),
                ),
                contracts,
            )
        else:
            rejected_applicant = reject_current_application(
                applicant=get_admitted_applicant(
                    applicants=applicants, applicant_id=marginal_applicant.applicant_id
                )
            )
            contract_with_new_applicant = add_admitted_applicant_to_contract(
                applicant=AdmittedApplicant(
                    applicant_id=proposer.id, priority_score=application.priority_score
                ),
                contract=remove_admitted_applicant_from_contract(
                    applicant_id=rejected_applicant.id, contract=proposed_contract
                ),
            )
            return self(
                update_applicants(
                    applicants=update_applicants(
                        applicants=applicants, applicant=rejected_applicant
                    ),
                    applicant=admit_next_application(applicant=proposer),
                ),
                {
                    **contracts,
                    contract_with_new_applicant.id: contract_with_new_applicant,
                },
            )

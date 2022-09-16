from python.get_applicants.libs.admint_next_application import admit_next_application
from python.get_applicants.libs.get_marginal_admitted_applicant import (
    get_marginal_admitted_applicant,
)
from python.get_applicants.libs.get_next_application import get_next_application
from python.get_applicants.libs.get_next_proposer import get_next_proposer
from python.get_applicants.libs.has_marginal_applicant import is_contract_full
from python.get_applicants.libs.has_proposer import has_proposer
from python.get_applicants.libs.add_admitted_applicant_to_contract import (
    add_admitted_applicant_to_contract,
)
from python.get_applicants.libs.reject_next_application import reject_next_application
from python.get_applicants.libs.remove_admitted_applicant_from_contract import (
    remove_admitted_applicant_from_contract,
)
from python.get_applicants.types import Applicants, Contacts, AdmittedApplicant


def get_applicants_rec(applicants: Applicants, contracts: Contacts) -> Applicants:
    if not has_proposer(applicants=applicants):
        return applicants

    proposer = get_next_proposer(applicants=applicants)
    application = get_next_application(applicant=proposer)
    proposed_contract = contracts.get(application.contract)
    if not is_contract_full(contract=proposed_contract):
        admitted_applicant = admit_next_application(applicant=proposer)
        contract_with_new_applicant = add_admitted_applicant_to_contract(
            applicant=AdmittedApplicant(
                applicant_id=proposer.id, priority_score=application.priority_score
            ),
            contract=proposed_contract,
        )
        return get_applicants_rec(
            applicants={**applicants, admitted_applicant.id: admitted_applicant},
            contracts={
                **contracts,
                contract_with_new_applicant.id: contract_with_new_applicant,
            },
        )
    else:
        marginal_applicant = get_marginal_admitted_applicant(contract=proposed_contract)
        if marginal_applicant.priority_score > application.priority_score:
            rejected_applicant = reject_next_application(applicant=proposer)
            return get_applicants_rec(
                applicants={**applicants, rejected_applicant.id: rejected_applicant},
                contracts=contracts,
            )
        else:
            rejected_applicant = reject_next_application(
                applicant=applicants.get(marginal_applicant.applicant_id)
            )
            admitted_applicant = admit_next_application(applicant=proposer)
            contract_with_new_applicant = add_admitted_applicant_to_contract(
                applicant=AdmittedApplicant(
                    applicant_id=proposer.id, priority_score=application.priority_score
                ),
                contract=remove_admitted_applicant_from_contract(
                    applicant_id=rejected_applicant.id, contract=proposed_contract
                ),
            )
            return get_applicants_rec(
                applicants={
                    **applicants,
                    rejected_applicant.id: rejected_applicant,
                    admitted_applicant.id: admitted_applicant,
                },
                contracts={
                    **contracts,
                    contract_with_new_applicant.id: contract_with_new_applicant,
                },
            )

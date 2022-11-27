from typing import Callable

from python.correct_dominated_choices.libs.correct_dominated_choices import (
    correct_dominated_choices,
)
from python.correct_dominated_choices.libs.get_state_funded_application_pair import (
    get_state_funded_application_pair,
)
from python.correct_dominated_choices.libs.get_state_funded_pair_contract_id import (
    get_state_funded_pair_contract_id,
)
from python.correct_dominated_choices.libs.has_ranked import has_ranked
from python.correct_dominated_choices.libs.has_state_funded_pair import (
    has_state_funded_pair,
)
from python.types import Input, Contract, Applicant, Application

correct_dominated_choices_lower: Callable[
    [Input], Input
] = lambda input: correct_dominated_choices(
    input=input, get_corrected_applicant=_get_corrected_applicant
)


def _get_corrected_applicant(
    programs: dict, contracts: dict[str, Contract], applicant: Applicant
) -> Applicant:
    fixed_ranked_applications: list[Application] = []
    for application in applicant.ranked_applications:
        is_already_ranked = has_ranked(
            contract_id=application.contract,
            ranked_applications=fixed_ranked_applications,
        )
        if is_already_ranked:
            continue
        contract = contracts[application.contract]
        if not contract.state_funded and has_state_funded_pair(
            contract=contract, programs=programs
        ):
            state_funded_pair_contract_id = get_state_funded_pair_contract_id(
                programs=programs, contract=contract
            )
            is_state_funded_pair_in_fixed_ranked_applications = has_ranked(
                contract_id=state_funded_pair_contract_id,
                ranked_applications=fixed_ranked_applications,
            )
            if not is_state_funded_pair_in_fixed_ranked_applications:
                fixed_ranked_applications.append(
                    get_state_funded_application_pair(
                        state_funded_contract_id=state_funded_pair_contract_id,
                        applicant=applicant,
                        application=application,
                    )
                )
        fixed_ranked_applications.append(application)
    return Applicant(
        id=applicant.id,
        status=applicant.status,
        ranked_applications=fixed_ranked_applications,
    )

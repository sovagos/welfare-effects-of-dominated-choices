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

correct_dominated_choices_upper: Callable[
    [Input], Input
] = lambda input: correct_dominated_choices(
    input=input, get_corrected_applicant=_get_corrected_applicant
)


def _get_corrected_applicant(
    programs: dict, contracts: dict[str, Contract], applicant: Applicant
) -> Applicant:
    moved_up_applications = []
    in_place_applications: list[Application] = []
    for application in applicant.ranked_applications:
        contract = contracts[application.contract]
        is_moved_up = has_ranked(
            contract_id=application.contract,
            ranked_applications=moved_up_applications,
        )
        if is_moved_up:
            continue
        if contract.state_funded:
            in_place_applications.append(application)
            continue
        in_place_applications.append(application)
        if has_state_funded_pair(programs=programs, contract=contract):
            state_funded_pair_contract_id = get_state_funded_pair_contract_id(
                programs=programs, contract=contract
            )
            if not has_ranked(
                contract_id=state_funded_pair_contract_id,
                ranked_applications=in_place_applications,
            ):
                moved_up_applications.append(
                    get_state_funded_application_pair(
                        state_funded_contract_id=state_funded_pair_contract_id,
                        applicant=applicant,
                        application=application,
                    )
                )
    return Applicant(
        id=applicant.id,
        status=applicant.status,
        ranked_applications=[*moved_up_applications, *in_place_applications],
    )

from typing import Any

from python.correct_dominated_choices.libs.has_ranked import has_ranked
from python.types import Application, Applicant


def get_state_funded_application_pair(
    state_funded_contract_id: str, applicant: Applicant, application: Application
) -> Application:
    is_flipping = has_ranked(
        contract_id=state_funded_contract_id,
        ranked_applications=applicant.ranked_applications,
    )
    if is_flipping:
        return _get_application_by_contract_id(
            ranked_applications=applicant.ranked_applications,
            contract_id=state_funded_contract_id,
        )
    return Application(
        contract=state_funded_contract_id,
        priority_score=application.priority_score,
        admitted=False,
    )


def _get_application_by_contract_id(
    ranked_applications: list[Application], contract_id: str
) -> Any:
    for application in ranked_applications:
        if application.contract == contract_id:
            return application

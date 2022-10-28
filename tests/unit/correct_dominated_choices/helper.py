from python.types import Applicant
from tests.unit.helpers import create_applicant, create_application


def create_applicant_with_ranked_applications(contract_ids: list[str]) -> Applicant:
    return create_applicant(
        {
            "id": "x",
            "ranked_applications": [
                create_application({"contract": contract_id, "priority_score": 0})
                for contract_id in contract_ids
            ],
        }
    )

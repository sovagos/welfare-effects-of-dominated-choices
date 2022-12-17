from python.types import Applicant
from tests.helpers import create_applicant, create_application


def create_applicant_with_ranked_applications(pairs: list[dict]) -> Applicant:
    return create_applicant(
        {
            "id": "x",
            "ranked_applications": [
                create_application(
                    {
                        "contract": pair["contract_id"],
                        "admitted": pair["admitted"],
                        "priority_score": 0,
                    }
                )
                for pair in pairs
            ],
        }
    )

from python.get_matching.get_matching_from_applicant import get_matching_from_applicant
from tests.helpers import (
    create_applicant,
    get_random_string,
    create_application,
    create_admitted_applicant_status,
    create_matching,
    create_rejected_applicant_status,
)


def test__get_matching_from_applicant__when_applicant_is_admitted__returns_right_matching():
    applicant_id = get_random_string()
    contract_id = get_random_string()
    rank_of_admission = 1
    applicant = create_applicant(
        {
            "id": applicant_id,
            "ranked_applications": [create_application({"contract": contract_id})],
            "status": create_admitted_applicant_status({"rank": rank_of_admission}),
        }
    )

    result = get_matching_from_applicant(applicant=applicant)

    assert result == create_matching(
        {
            "applicant_id": applicant_id,
            "contract_id": contract_id,
            "rank": rank_of_admission,
        }
    )


def test__get_matching_from_applicant__when_applicant_is_rejected__returns_right_matching():
    applicant_id = get_random_string()
    contract_id = get_random_string()
    rank_of_admission = 2
    applicant = create_applicant(
        {
            "id": applicant_id,
            "ranked_applications": [create_application({"contract": contract_id})],
            "status": create_rejected_applicant_status({"rank": rank_of_admission}),
        }
    )

    result = get_matching_from_applicant(applicant=applicant)

    assert result == create_matching(
        {
            "applicant_id": applicant_id,
            "contract_id": "Unassigned",
            "rank": 0,
        }
    )

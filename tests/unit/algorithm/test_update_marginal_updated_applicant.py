from python.algorithm.update_marginal_admitted_applicant import (
    update_marginal_admitted_applicant,
)
from tests.unit.algorithm.helpers import (
    create_applicant,
    create_admitted_applicant,
    create_rejected_applicant_status,
    create_admitted_applicant_status,
)


def test__update_marginal_admitted_applicant__updates_marginal_updated_applicant_to_rejected_applicant():
    applicant_1 = create_applicant()
    applicant_2 = create_applicant(
        {"status": create_admitted_applicant_status({"rank": 1})}
    )
    applicant_3 = create_applicant()
    applicants = [applicant_1, applicant_2, applicant_3]
    marginal_admitted_applicant = create_admitted_applicant(
        {"applicant_id": applicant_2.id}
    )

    expected_result = create_applicant(
        {
            "id": applicant_2.id,
            "ranked_applications": applicant_2.ranked_applications,
            "status": create_rejected_applicant_status({"rank": 1}),
        }
    )

    result = update_marginal_admitted_applicant(
        applicants=applicants, marginal_admitted_applicant=marginal_admitted_applicant
    )

    assert result == expected_result

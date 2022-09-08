from python.algorithm.update_applicants_with_proposer import (
    update_applicants_with_proposer,
)
from tests.unit.algorithm.helpers import create_applicant, create_application


def test__update_applicants_with_proposer__when_single_applicant_is_the_proposer__return_update_proposer():
    applicant = create_applicant({"ranked_applications": create_application()})
    applicants = [applicant]
    proposer = create_applicant({"id": applicant.id})

    result = update_applicants_with_proposer(applicants=applicants, proposer=proposer)

    assert result == [proposer]


def test__update_applicants_with_proposer__when_there_are_multiple_applicants__return_list_of_applicants_including_the_proposer():
    applicant_1 = create_applicant({"ranked_applications": create_application()})
    applicant_2 = create_applicant({"ranked_applications": create_application()})
    applicant_3 = create_applicant({"ranked_applications": create_application()})
    applicants = [applicant_1, applicant_2, applicant_3]
    proposer = create_applicant(
        {"id": applicant_2.id, "ranked_applications": create_application()}
    )

    result = update_applicants_with_proposer(applicants=applicants, proposer=proposer)

    assert result == [applicant_1, proposer, applicant_3]

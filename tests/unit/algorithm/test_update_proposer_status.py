from python.algorithm.applicant import ApplicantStatusType
from python.algorithm.update_proposer import update_proposer
from tests.unit.algorithm.helpers import (
    create_applicant,
    create_rejected_applicant_status,
)


def test__update_proposer__when_status_is_initial__update_admitted_applicant_status_to_rank_of_one():
    applicant = create_applicant()

    result = update_proposer(applicant=applicant)

    assert result.status.type == ApplicantStatusType.ADMITTED
    assert result.status.rank == 1


def create_applicantion():
    pass


def test__update_proposer__when_status_is_rejected__update_status_to_next_contract():
    application_1 = create_applicantion()
    application_2 = create_applicantion()
    applicant = create_applicant(
        {
            "ranked_applications": [application_1, application_2],
            "status": create_rejected_applicant_status({"rank": 1}),
        }
    )

    result = update_proposer(applicant=applicant)

    assert result.status.type == ApplicantStatusType.ADMITTED
    assert result.status.rank == 2

from python.get_matching.libs.update_applicants import update_applicants
from tests.unit.helpers import (
    create_applicants,
    get_random_string,
    create_applicant,
    create_admitted_applicant_status,
    create_rejected_applicant_status,
    create_application,
)


def test__update_applicants__admitted_applicant_given__adds_to_admitted() -> None:
    applicant_id = get_random_string()
    applicants = create_applicants({"admitted": {}})
    applicant = create_applicant(
        {"id": applicant_id, "status": create_admitted_applicant_status()}
    )

    result = update_applicants(applicants=applicants, applicant=applicant)

    assert result.admitted[applicant_id] == applicant


def test__update_applicants__admitted_applicant_given__update_the_admitted_applicant() -> None:
    applicant_id = get_random_string()
    applicants = create_applicants(
        {"admitted": {applicant_id: create_applicant({"id": applicant_id})}}
    )
    applicant = create_applicant(
        {"id": applicant_id, "status": create_admitted_applicant_status()}
    )

    result = update_applicants(applicants=applicants, applicant=applicant)

    assert result.admitted[applicant_id] == applicant


def test__update_applicants__admitted_applicant_given__remove_from_proposer() -> None:
    applicant_id = get_random_string()
    proposer_applicant = create_applicant({"id": applicant_id})
    applicants = create_applicants({"proposer": [proposer_applicant]})
    admitted_applicant = create_applicant(
        {"id": applicant_id, "status": create_admitted_applicant_status()}
    )

    result = update_applicants(applicants=applicants, applicant=admitted_applicant)

    assert proposer_applicant not in result.proposer


def test__update_applicants__exhausted_applicant_given__adds_to_exhausted() -> None:
    applicants = create_applicants({"exhausted": []})
    exhausted_applicant = create_applicant(
        {
            "ranked_applications": [create_application()],
            "status": create_rejected_applicant_status({"rank": 1}),
        }
    )

    result = update_applicants(applicants=applicants, applicant=exhausted_applicant)

    assert exhausted_applicant in result.exhausted


def test__update_applicants__exhausted_applicant_given__removes_from_proposer() -> None:
    applicant_id = get_random_string()
    proposer_applicant = create_applicant({"id": applicant_id})
    applicants = create_applicants({"proposer": [proposer_applicant]})
    exhausted_applicant = create_applicant(
        {
            "id": applicant_id,
            "ranked_applications": [create_application()],
            "status": create_rejected_applicant_status({"rank": 1}),
        }
    )

    result = update_applicants(applicants=applicants, applicant=exhausted_applicant)

    assert exhausted_applicant not in result.proposer


def test__update_applicants__exhausted_applicant_given__removes_from_admitted() -> None:
    applicant_id = get_random_string()
    admitted_applicant = create_applicant({"id": applicant_id})
    applicants = create_applicants({"admitted": {applicant_id: admitted_applicant}})
    exhausted_applicant = create_applicant(
        {
            "id": applicant_id,
            "ranked_applications": [create_application()],
            "status": create_rejected_applicant_status({"rank": 1}),
        }
    )

    result = update_applicants(applicants=applicants, applicant=exhausted_applicant)

    assert applicant_id not in result.admitted.keys()


def test__update_applicants__proposer_applicant_given__adds_to_proposer_as_last_item() -> None:
    applicant_id = get_random_string()
    applicants = create_applicants({"proposer": [create_applicant()]})
    applicant = create_applicant(
        {
            "id": applicant_id,
            "ranked_applications": [create_application(), create_application()],
            "status": create_rejected_applicant_status({"rank": 1}),
        }
    )

    result = update_applicants(applicants=applicants, applicant=applicant)

    assert result.proposer[1] == applicant


def test__update_applicants__proposer_applicant_given__removes_from_admitted() -> None:
    applicant_id = get_random_string()
    applicants = create_applicants(
        {
            "admitted": {applicant_id: create_applicant({"id": applicant_id})},
            "proposer": [],
        }
    )
    applicant = create_applicant(
        {
            "id": applicant_id,
            "ranked_applications": [create_application(), create_application()],
            "status": create_rejected_applicant_status({"rank": 1}),
        }
    )

    result = update_applicants(applicants=applicants, applicant=applicant)

    assert applicant_id not in result.admitted.keys()


def test__update_applicants__proposer_applicant_given__updates_the_same_applicant_in_proposer() -> None:
    applicant_id = get_random_string()
    applicants = create_applicants(
        {"proposer": [create_applicant({"id": applicant_id}), create_applicant()]}
    )
    updated_applicant = create_applicant(
        {
            "id": applicant_id,
            "ranked_applications": [create_application(), create_application()],
            "status": create_rejected_applicant_status({"rank": 1}),
        }
    )

    result = update_applicants(applicants=applicants, applicant=updated_applicant)

    assert len([_ for _ in result.proposer if _.id == applicant_id]) == 1
    assert updated_applicant in result.proposer

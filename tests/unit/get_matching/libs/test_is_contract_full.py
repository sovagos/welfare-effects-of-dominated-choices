from python.get_matching.libs.has_marginal_applicant import (
    is_contract_full,
)
from tests.unit.helpers import create_application, create_contract


def test__is_contract_full__it_is_empty__returns_false() -> None:
    contract = create_contract({"capacity": 2, "admitted_applicants": []})

    result = is_contract_full(contract=contract)

    assert result is False


def test__is_contract_full__it_is_full__returns_true() -> None:
    contract = create_contract(
        {
            "capacity": 2,
            "admitted_applicants": [create_application(), create_application()],
        }
    )

    result = is_contract_full(contract=contract)

    assert result is True

from python.contract import Contract
from python.config import CAPACITY_MIN, PRIORITY_SCORE_CUTOFF_MIN, CAPACITY_FACTOR


def test_whether_contract_has_right_contract_id():
    contract = Contract("C1")

    assert contract.contract_id == "C1"


def test_when_priority_score_cutoff_is_low__then_add_capacity__returns_a_large_value():
    contract = Contract("C1")
    contract.priority_score_cutoff = PRIORITY_SCORE_CUTOFF_MIN
    contract.total_admitted = 10
    contract.add_capacity()

    assert contract.capacity > contract.total_admitted


def test_when_priority_score_cutoff_is_high__then_add_capacity__returns_total_admitted():
    contract = Contract("C1")
    contract.priority_score_cutoff = PRIORITY_SCORE_CUTOFF_MIN + 1
    contract.total_admitted = 10
    contract.add_capacity()

    assert contract.capacity == contract.total_admitted

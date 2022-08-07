import pytest
from python.contract import Contract
from python.matching_utils import compute_priority_score_cutoffs_from_matching


contracts = {
        "C1": Contract("C1"),
        "C2": Contract("C2")
    }
contracts["C1"].score_dictionary = {
    "A1": 10,
    "A2": 20
    }
contracts["C2"].score_dictionary = {
    "A1": 10,
    "A2": 20
    }


use_cases = [
    {
        "matching": {
            "A1": None,
            "A2": None
        },
        "expected": {
            "C1": 0,
            "C2": 0
        }
    },
    {
        "matching": {
            "A1": "C1",
            "A2": "C2"
        },
        "expected": {
            "C1": 10,
            "C2": 20
        }
    },
    
]

@pytest.mark.parametrize("use_case", use_cases)
def test__compute_priority_score_cutoffs__normal_matching__returns_right_cutoffs(use_case):
    matching = use_case["matching"]

    priroty_score_cutoffs = compute_priority_score_cutoffs_from_matching(matching, contracts)

    assert priroty_score_cutoffs == use_case["expected"]

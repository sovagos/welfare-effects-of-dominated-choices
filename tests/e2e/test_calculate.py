import pytest
import pandas as pd
from python.calculate import calculate


use_cases = [
    {
        "input": {
            "applicant_id": ["A1", "A1", "A1"],
            "rank": [1, 2, 3],
            "program_id": ["P1", "P1", "P2"],
            "contract_id": ["C1", "C2", "C3"],
            "state_funded": [True, False, True],
            "priority_score": [10, 10, 11],
            "capacity": [1, 1, 1],
        },
        "expected": {"C1": 10, 
                     "C2": 0,
                     "C3": 0
        },
    },
    {
        "input": {
            "applicant_id": ["A1", "A1", "A2"],
            "rank": [1, 2, 1],
            "program_id": ["P1", "P1", "P1"],
            "contract_id": ["C1", "C2", "C1"],
            "state_funded": [True, False, True],
            "priority_score": [11, 11, 9],
            "capacity": [1, 1, 1],
        },
        "expected": {"C1": 11,
                     "C2": 0
        }
    },
    {
        "input": {
            "applicant_id": ["A1", "A1", "A1", "A2", "A3"],
            "rank": [1, 2, 3, 1, 1],
            "program_id": ["P1", "P1", "P2", "P1", "P1"],
            "contract_id": ["C1", "C2", "C3", "C1", "C2"],
            "state_funded": [True, False, True, True, False],
            "priority_score": [10, 10, 10, 11, 11],
            "capacity": [1, 1, 1, 1, 1],
        },
        "expected": {
            "C1": 11,
            "C2": 11,
            "C3": 10
        }
    },
    {
        "input": {
            "applicant_id": ["A1", "A2", "A3"],
            "rank": [1, 1, 1],
            "program_id": ["P1", "P2", "P3"],
            "contract_id": ["C1", "C2", "C3"],
            "state_funded": [True, True, True],
            "priority_score": [9, 10, 11],
            "capacity": [1, 1, 1],
        },
        "expected": {
            "C1": 9,
            "C2": 10,
            "C3": 11
        }
    },
    {
        "input": {
            "applicant_id": ["A1", "A2", "A3"],
            "rank": [1, 1, 1],
            "program_id": ["P1", "P1", "P1"],
            "contract_id": ["C1", "C1", "C1"],
            "state_funded": [True, True, True],
            "priority_score": [11, 10, 9],
            "capacity": [2, 2, 2],
        },
        "expected": {
            "C1": 10
        }
    },
]


@pytest.mark.parametrize("use_case", use_cases)
def test__calculate__empty_input__returns_empty_list(use_case):
    data = pd.DataFrame(data=use_case["input"])

    result = calculate(data=data)

    assert result == use_case["expected"]

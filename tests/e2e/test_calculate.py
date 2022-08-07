import pytest
import pandas as pd
from python.calculate import calculate


use_cases = [
    {
        "input": {
            "applicant_id": [],
            "rank": [],
            "program_id": [],
            "contract_id": [],
            "state_funded": [],
            "priority_score": [],
            "capacity": [],
        },
        "expected": {}
    }
]


@pytest.mark.parametrize("use_case", use_cases)
def test__calculate__empty_input__returns_empty_list(use_case):
    data = pd.DataFrame(data=use_case["input"])

    result = calculate(data=data)

    assert result == use_case["expected"]

import pandas as pd
import pytest

from python.validate_data import validate_data


def test__validate_data__data_has_relevant_column__returns_no_exception():
    data = pd.DataFrame(
        {'applicant_id': ["A1", "A1"],
         'rank': [1, 2],
         'program_id': ["P1", "P1"],
         'contract_id': ["C1", "C2"],
         'state_funded': [True, False],
         'priority_score': [1, 2],
         'capacity': [1, 1]
         }
    )

    validate_data(
        data=data
    )


def test__validate_data__data_has_relevant_column__returns_no_exception():
    data = pd.DataFrame(
        {'applicant_id': []}
    )

    with pytest.raises(ValueError, match="The data has no rows"):
        validate_data(data=data)


def test__validate_data__data_has_relevant_column__returns_key_error():
    data = pd.DataFrame(
        {'applicant_id': ["A1", "A1"],
         'program_id': ["P1", "P1"],
         'contract_id': ["C1", "C2"],
         'state_funded': [True, False],
         'priority_score': [1, 2],
         'capacity': [1, 1]
         }
    )

    with pytest.raises(KeyError, match="The data does not have rank column"):
        validate_data(data=data)


def test__validate_data__column_has_incorrect_type__returns_type_error():
    data = pd.DataFrame(
        {'applicant_id': [1, 1],
         'rank': [1, 2],
         'program_id': ["P1", "P1"],
         'contract_id': ["C1", "C2"],
         'state_funded': [True, False],
         'priority_score': [1, 2],
         'capacity': [1, 1]
         }
    )

    with pytest.raises(TypeError, match=f"The type of applicant_id is not object"):
        validate_data(data=data)


def test__validate_data__data_has_a_duplicated_column__returns_value_error():
    data = pd.DataFrame(
        {'applicant_id': ["A1", "A1"],
         'rank': [1, 1],
         'program_id': ["P1", "P1"],
         'contract_id': ["C1", "C2"],
         'state_funded': [True, False],
         'priority_score': [1, 2],
         'capacity': [1, 1]
         }
    )

    with pytest.raises(ValueError, match="There are duplicates in the data"):
         validate_data(data=data)


def test__validate_data__contract_level_data_has_a_duplicated_column__returns_value_error():
    data = pd.DataFrame(
        {'applicant_id': ["A1", "A1", "A2"],
         'rank': [1, 2, 1],
         'program_id': ["P1", "P1", "P1"],
         'contract_id': ["C1", "C2", "C1"],
         'state_funded': [True, False, False],
         'priority_score': [1, 2, 3],
         'capacity': [1, 1, 1]
         }
    )

    with pytest.raises(ValueError, match="There are inconsistencies in the contract-level data"):
         validate_data(data=data)

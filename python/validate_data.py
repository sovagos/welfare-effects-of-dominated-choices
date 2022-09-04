import pandas as pd
from python.data_validation_config import (
    DATA_SCHEMA,
    UNIQUE_COLUMN_COMBINATIONS_FOR_APPLICANTS,
    UNIQUE_COLUMN_COMBINATIONS_FOR_CONTRACTS,
    CONTRACT_KEYS,
)


def validate_data(data: pd.DataFrame) -> None:
    _check_whether_dataframe_has_rows(data)
    _check_whether_data_has_right_schema(data)
    _check_unique_keys(data)
    data_contracts = _collapse_data_to_contract_level(data)
    _check_whether_contract_data_is_consistent(data_contracts)


def _check_whether_dataframe_has_rows(data: pd.DataFrame) -> None:
    if data.shape[0] == 0:
        raise ValueError("The data has no rows")


def _check_whether_data_has_right_schema(data: pd.DataFrame) -> None:
    for colname, col_type in DATA_SCHEMA.items():
        _check_whether_dataframe_has_column(data=data, colname=colname)
        _check_whether_column_has_the_right_type(
            data=data, colname=colname, col_type=col_type
        )


def _check_whether_dataframe_has_column(data: pd.DataFrame, colname: str) -> None:
    if colname not in data.columns:
        raise KeyError(f"The data does not have {colname} column")


def _check_whether_column_has_the_right_type(
    data: pd.DataFrame, colname: str, col_type: str
) -> None:
    if data[colname].dtype != col_type:
        raise TypeError(f"The type of {colname} is not {col_type}")


def _check_unique_keys(data: pd.DataFrame) -> None:
    for key_column_names in UNIQUE_COLUMN_COMBINATIONS_FOR_APPLICANTS:
        if data.drop_duplicates(subset=key_column_names).shape[0] != data.shape[0]:
            raise ValueError("There are duplicates in the data")


def _collapse_data_to_contract_level(data: pd.DataFrame) -> pd.DataFrame:
    return data[CONTRACT_KEYS].drop_duplicates().reset_index()


def _check_whether_contract_data_is_consistent(data: pd.DataFrame) -> None:
    for key_column_names in UNIQUE_COLUMN_COMBINATIONS_FOR_CONTRACTS:
        if data.drop_duplicates(subset=key_column_names).shape[0] != data.shape[0]:
            raise ValueError("There are inconsistencies in the contract-level data")

import pandas as pd
from python.config import DATA_SCHEMA, UNIQUE_COLUMN_COMBINATIONS_FOR_APPLICANTS, UNIQUE_COLUMN_COMBINATIONS_FOR_CONTRACTS
from python.data_utils import check_unique_keys, check_whether_column_has_the_right_type

def validate_data(data):
    """ Validate input data

    Args:
        data (data.frame): input data
    
    Returns:
        KeyError when column is missing, prints message otherwise
        KeyError when one of the columns is missing, prints message otherwise
    """
    for colname, col_type in DATA_SCHEMA.items():
        check_whether_column_has_the_right_type(data, colname, col_type)
    for key_column_names in UNIQUE_COLUMN_COMBINATIONS_FOR_APPLICANTS:
        check_unique_keys(data, key_column_names)
    data_contracts = data[['program_id', 'contract_id', 'state_funded', 'capacity']].drop_duplicates().reset_index()
    for key_column_names in UNIQUE_COLUMN_COMBINATIONS_FOR_CONTRACTS:
        check_unique_keys(data_contracts, key_column_names)

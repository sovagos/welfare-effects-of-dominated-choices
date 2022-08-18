import pandas as pd
from python.applicant import Applicant
from python.contract import Contract
from python.program import Program

def create_applicants(data):
    n_rows = len(data)
    applicant_ids = data['applicant_id'].unique()
    applicants = {}
    for a in applicant_ids:
        applicant = Applicant(a)
        applicants[a] = applicant    
    for d in range(n_rows):
        applicant_id = data["applicant_id"][d]
        applicant = applicants[applicant_id]
        applicant.ranking.append([int(data["rank"][d]), data["contract_id"][d]])
        applicant.priority_scores.append([int(data["rank"][d]), data["priority_score"][d]])
        # if data["admitted"][d] == 1:
        #     applicant.realized_admitted = data["contract_id"][d]
    return applicants

def create_contracts(data):
    data_contracts = data[['program_id', 'contract_id', 'state_funded', 'capacity']].drop_duplicates().reset_index()
    contract_ids = pd.unique(data_contracts["contract_id"])
    contracts = {}
    for c in contract_ids:
        contracts[c] = Contract(c)
    for d in range(len(data_contracts)):
        contract_id = data_contracts["contract_id"][d]
        contracts[contract_id].program_id = data_contracts["program_id"][d]
        contracts[contract_id].state_funded = data_contracts["state_funded"][d]
        contracts[contract_id].capacity = data_contracts["capacity"][d]
        #contracts[contract_id].priority_score_cutoff = int(data["priority_score_cutoff"][d])
    return contracts

def create_programs(contracts):
    programs = {}
    program_ids = {contract.program_id for contract in contracts.values()}
    for program_id in program_ids:
        programs[program_id] = Program(program_id, [contract for contract in contracts.values() \
            if contract.program_id == program_id])
    return programs


def check_whether_column_has_the_right_type(data, colname, col_type):
    """ Check whether a column has the right type

    Args:
        data (data.frame): input data
        colname (str): column name
        col_type (str): column type

    Retruns:
        KeyError when column is missing, prints message otherwise
    """
    try:
        if data[colname].dtype == col_type:
            print(f"Column {colname} has the right type ({col_type}).")
        else:
            print(f"Column {colname} does not have the right type.")
    except KeyError:
        print(f"The dataset does not have {colname} columns.")


def check_unique_keys(data, key_column_names):
    """ Check whether certain combination of columns define a unique row in the dataset

    Args:
        data (data.frame): input data
        key_column_names (list): list of column names

    Returns:
        KeyError when one of the columns is missing, prints message otherwise
    """
    try:
        if data.drop_duplicates(subset = key_column_names).shape[0] == data.shape[0]:
            print(f"The dataset is unique by {key_column_names}.")
        else:
            print(f"The dataset is not unique by {key_column_names}.")
    except KeyError:
        print(f"The dataset does not have {key_column_names} columns.")
        

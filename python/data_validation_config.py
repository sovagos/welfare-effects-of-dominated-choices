DATA_SCHEMA = {
    "applicant_id": "object",
    "rank": "int",
    "program_id": "object",
    "contract_id": "object",
    "state_funded": "bool",
    "priority_score": "int",
    "capacity": "int",
}

CONTRACT_KEYS = ["program_id", "contract_id", "state_funded", "capacity"]

UNIQUE_COLUMN_COMBINATIONS_FOR_APPLICANTS = [
    ["applicant_id", "rank"],
    ["applicant_id", "contract_id"],
    ["applicant_id", "program_id", "state_funded"],
]

UNIQUE_COLUMN_COMBINATIONS_FOR_CONTRACTS = [
    ["contract_id"],
    ["program_id", "state_funded"],
]

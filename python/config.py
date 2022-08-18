
PRIORITY_SCORE_CUTOFF_MIN = float(5)
CAPACITY_FACTOR  = 1.2
CAPACITY_MIN = 10
UNACCEPTABLE_SCORE = 3

DATA_SCHEMA = {
    "applicant_id": "object",
    "rank": "int",
    "program_id": "object",
    "contract_id": "object",
    "state_funded": "bool",
    "priority_score": "int",
    "capacity": "int"
}

UNIQUE_COLUMN_COMBINATIONS_FOR_APPLICANTS = [
    ["applicant_id", "rank"],
    ["applicant_id", "contract_id"],
    ["applicant_id", "program_id", "state_funded"],
]

UNIQUE_COLUMN_COMBINATIONS_FOR_CONTRACTS = [
    ["contract_id"],
    ["program_id", "state_funded"],
]
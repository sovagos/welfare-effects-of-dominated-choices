from enum import unique
from python.applicant import Applicant
from python.contract import Contract
from python.program import Program

import pandas as pd

d = {
        'applicant_id': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        'rank': [1, 2, 3, 1, 2, 3, 1, 2, 3],
        'program_id': [1, 1, 3, 1, 3, 3, 5, 3, 1],
        'state_funded': [1, 0, 0, 1, 0, 1, 1, 1, 1],
        'priority_score': [10, 11, 12, 13, 14, 15, 16, 17, 18],
        'admitted': [1, 0, 0, 0, 1, 0, 1, 0, 0]
    }
data = pd.DataFrame(data=d)
data["contract_id"] = data["program_id"] + (1 - data["state_funded"])

applicant_ids = data['applicant_id'].unique()
applicants = {}
for a in applicant_ids:
    applicant = Applicant(a)
    applicants[a] = applicant
    
n_rows = len(data)
for d in range(n_rows):
    applicant_id = data["applicant_id"][d]
    a = applicants[applicant_id]
    a.ranking.append([int(data["rank"][d]), data["contract_id"][d]])

for applicant_id in applicants:
    applicants[applicant_id].ranking.sort()
    applicants[applicant_id].ranking_sorted = [x[1] for x in applicants[applicant_id].ranking]

# Create contracts
contract_ids = pd.unique(data["contract_id"])
contracts = {}

for c in contract_ids:
    contracts[c] = Contract(c)

for d in range(n_rows):
    applicant_id = data["applicant_id"][d]
    contract_id = data["contract_id"][d]
    contracts[contract_id].program_id = data["program_id"][d]
    contracts[contract_id].state_funded = data["state_funded"][d]
    priority_score = int(data["priority_score"][d])
    contracts[contract_id].score_dictionary[d] = priority_score
    contracts[contract_id].ranking.append([priority_score, applicant_id])
    if data["admitted"][d] == 1:
        contracts[contract_id].total_admitted += 1

# Sort rankings
for contract in contracts.values():
    contract.ranking = sorted(contract.ranking)[::-1]

# Create programs
programs = {}
program_ids = {contract.program_id for contract in contracts.values()}
for program_id in program_ids:
    programs[program_id] = Program(program_id, [contract for contract in contracts.values() if contract.program_id == program_id])

# Next step: set capacities based on admitted students
# Add tests for classes
# refactor setting contracts, programs, applicants -> add functions with tests
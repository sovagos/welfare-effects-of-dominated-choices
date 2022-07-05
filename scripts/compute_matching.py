from heapq import heappop, heappush
import random
from python.applicant import Applicant
from python.config import CAPACITY_MIN, PRIORITY_SCORE_CUTOFF_MIN, CAPACITY_FACTOR
from python.contract import Contract
from python.matching_utils import STB, student_proposing_deferred_acceptance
from python.program import Program
import pandas as pd

d = {
        'applicant_id': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        'rank': [1, 2, 3, 1, 2, 3, 1, 2, 3],
        'program_id': [1, 1, 3, 1, 3, 3, 5, 3, 1],
        'state_funded': [1, 0, 0, 1, 0, 1, 1, 1, 1],
        'priority_score': [10, 11, 12, 13, 14, 15, 16, 17, 18],
        'admitted': [1, 0, 0, 0, 1, 0, 1, 0, 0],
        'priority_score_cutoff': [10, 5, 14, 10, 14, 5, 16, 5, 10],
    }
data = pd.DataFrame(data=d)
data["contract_id"] = data["program_id"] + (1 - data["state_funded"])
n_rows = len(data)


# Create applicants
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
    if data["admitted"][d] == 1:
        applicant.realized_admitted = data["contract_id"][d]

for applicant_id in applicants:
    applicants[applicant_id].ranking.sort()
    applicants[applicant_id].ranking_sorted = [x[1] for x in applicants[applicant_id].ranking]
    applicants[applicant_id].priority_scores.sort()
    applicants[applicant_id].priority_scores_sorted = [x[1] for x in applicants[applicant_id].priority_scores]

# Create contracts
contract_ids = pd.unique(data["contract_id"])
contracts = {}

for c in contract_ids:
    contracts[c] = Contract(c)

for d in range(n_rows):
    contract_id = data["contract_id"][d]
    contracts[contract_id].program_id = data["program_id"][d]
    contracts[contract_id].state_funded = data["state_funded"][d]
    contracts[contract_id].priority_score_cutoff = int(data["priority_score_cutoff"][d])


        
# Sort rankings
for contract in contracts.values():
    contract.ranking = sorted(contract.ranking)[::-1]

# Set capacities
for contract in contracts.values():
    if contract.priority_score_cutoff == PRIORITY_SCORE_CUTOFF_MIN:
        contract.capacity = max(contract.total_admitted*CAPACITY_FACTOR, CAPACITY_MIN)
    else:
        contract.capacity = contract.total_admitted
        

# Create programs
programs = {}
program_ids = {contract.program_id for contract in contracts.values()}
for program_id in program_ids:
    programs[program_id] = Program(program_id, [contract for contract in contracts.values() if contract.program_id == program_id])


# Add tests for classes
# refactor setting contracts, programs, applicants -> add functions with tests

# TODO: STB should only depend on the applicants
# TODO: Add function that updates score dictironary and ranking in contracts:
# TODO: needs refactoring
for contract in contracts.values():
    for applicant in applicants.values():
        if applicant.realized_admitted == contract.contract_id:
            contract.total_admitted += 1
        rankings = [ranking[0] for ranking in applicant.ranking if ranking[1] == contract.contract_id]
        for r in rankings:
            priority_score = applicant.priority_scores[r-1][1]
            contract.score_dictionary[applicant.applicant_id] = priority_score
            contract.ranking.append([priority_score, applicant.applicant_id])

STB(applicants)
matching = student_proposing_deferred_acceptance(applicants, contracts)





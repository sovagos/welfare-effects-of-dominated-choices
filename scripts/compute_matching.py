from heapq import heappop, heappush
import random
from python.applicant import Applicant
from python.config import CAPACITY_MIN, PRIORITY_SCORE_CUTOFF_MIN, CAPACITY_FACTOR
from python.contract import Contract
from python.matching_state import MatchingState
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
    priority_score = int(data["priority_score"][d])
    contracts[contract_id].program_id = data["program_id"][d]
    contracts[contract_id].state_funded = data["state_funded"][d]
    contracts[contract_id].score_dictionary[applicant_id] = priority_score
    contracts[contract_id].ranking.append([priority_score, applicant_id])
    if data["admitted"][d] == 1:
        contracts[contract_id].total_admitted += 1
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


def STB(applicants, contracts, seed = 1000):
    """Run single tie-breaking."""
    random.seed(seed)
    random_tiebreaker = {applicant_id : random.random() for applicant_id in applicants}
    for contract in contracts.values():    
        contract.score_dictionary = {applicant_id : contract.score_dictionary[applicant_id] + random_tiebreaker[applicant_id] for applicant_id in contract.score_dictionary.keys()}
        contract.ranking = sorted([[x[1],x[0]] for x in contract.score_dictionary.items()])[::-1]


STB(applicants, contracts)
matching_state = MatchingState(applicants, contracts)
matching = student_proposing_deferred_acceptance(applicants, contracts)




def student_proposing_deferred_acceptance(applicants, contracts):
    """Run Student-Proposing Deferred Acceptance."""
    matching_state = MatchingState(applicants, contracts)
    temp_mu = matching_state.temp_mu
    cutoffs = matching_state.cutoffs
    proposers = matching_state.proposers
    curr_inds = matching_state.curr_inds
    while len(proposers) > 0:
        applicant_id, applicant = proposers.pop()
        contract_id = applicant.ranking_sorted[curr_inds[applicant_id]]
        # Rejected applicant
        while contracts[contract_id].score_dictionary[applicant_id] < cutoffs[contract_id] or \
              contracts[contract_id].score_dictionary[applicant_id] < PRIORITY_SCORE_CUTOFF_MIN:
            curr_inds[applicant_id] += 1
            if curr_inds[applicant_id] == len(applicant.ranking_sorted):
                contract_id = None
                break
            contract_id = applicant.ranking_sorted[curr_inds[applicant_id]]
        if contract_id == None: continue
        # Update assignment
        heappush(temp_mu[contract_id], (contracts[contract_id].score_dictionary[applicant_id], applicant_id))
        # 
        if len(temp_mu[contract_id]) > contracts[contract_id].capacity:
            min_s = heappop(temp_mu[contract_id])
            applicant_id_out = min_s[1]
            curr_inds[applicant_id_out] += 1
            if curr_inds[applicant_id_out] < len(applicants[applicant_id_out].ranking_sorted):
                proposers.add((applicant_id_out, applicants[applicant_id_out]))
            cutoffs[contract_id] = min_s[0] + 10**(-10)  
    matching = {applicant_id : None for applicant_id in applicants}
    for contract_id in temp_mu:
        for sc_applicant_id in temp_mu[contract_id]:
            applicant_id = sc_applicant_id[1]
            matching[applicant_id] = contract_id
    return matching

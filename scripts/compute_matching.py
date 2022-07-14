from heapq import heappop, heappush
import random
from types import NoneType
from python.applicant import Applicant
from python.config import CAPACITY_MIN, PRIORITY_SCORE_CUTOFF_MIN, CAPACITY_FACTOR
from python.contract import Contract
from python.data_utils import createApplicants, createContracts, createPrograms
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

# Create applicants
applicants = createApplicants(data)

# Create contracts and add capacities
contracts = createContracts(data)
for contract in contracts.values():
    contract.add_capacity()

# Create programs
programs = createPrograms(contracts)

for applicant_id in applicants:
    applicants[applicant_id].ranking.sort()
    applicants[applicant_id].ranking_sorted = [x[1] for x in applicants[applicant_id].ranking]
    applicants[applicant_id].priority_scores.sort()
    applicants[applicant_id].priority_scores_sorted = [x[1] for x in applicants[applicant_id].priority_scores]


# TODO: use createSelfFundedProgramDictionary and add test
dual_program_dictionary = {program.self_funded.contract_id: program.state_funded.contract_id for program in programs.values() if (program.self_funded != None) & (program.state_funded != None)}


# Add dominated dropping
for applicant in applicants.values():
    applicant.add_dominated_dropping(dual_program_dictionary)


# TODO: add dominated flipping
# TODO: print statistics on dominated choices
# TODO: correct dominated choices

# Add tests for classes
# refactor setting contracts, programs, applicants -> add functions with tests
# TODO: Add function that updates score dictionary and ranking in contracts:

for applicant in applicants.values():
    contracts[applicant.realized_admitted].total_admitted += 1
    ranking_with_priority_score = list(
        zip(
            [ranking for ranking in applicant.ranking_sorted],
            [applicant.applicant_id]*len(applicant.ranking_sorted),
            [priority_score for priority_score in applicant.priority_scores_sorted],
            )
        )
    for r in ranking_with_priority_score:
        contracts[r[0]].score_dictionary[r[1]] = r[2]

# TODO: turn into a class method: addScoreDictionary(self, applicants) {}
# Usage: for contract in contracts: contract.addScoreDictionary(applicants)

STB(applicants)
matching = student_proposing_deferred_acceptance(applicants, contracts)





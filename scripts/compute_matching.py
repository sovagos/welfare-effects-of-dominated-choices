from heapq import heappop, heappush
import random
from types import NoneType
from python.applicant import Applicant
from python.contract import Contract
from python.program import Program
from python.config import CAPACITY_MIN, PRIORITY_SCORE_CUTOFF_MIN, CAPACITY_FACTOR
from python.data_utils import create_applicants, create_contracts, create_programs
from python.matching_utils import STB, student_proposing_deferred_acceptance, summarize_dominated_choices
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
applicants = create_applicants(data)

# Create contracts and add capacities
contracts = create_contracts(data)
for contract in contracts.values():
    contract.add_capacity()

# Add realized admitted to contracts
for applicant in applicants.values():
    contracts[applicant.realized_admitted].total_admitted += 1

# Create programs
programs = create_programs(contracts)

# Create dual self funded dictionary
dual_self_funded_program_dictionary = {}
for program in programs.values():
    dual_self_funded_program_dictionary.update(program.create_self_funded_program_dictionary())

# Add and summarize dominated choices
for applicant in applicants.values():
    applicant.add_dominated_dropping(dual_self_funded_program_dictionary)
    applicant.add_dominated_flipping(dual_self_funded_program_dictionary)
summarize_dominated_choices(applicants)

# Correct dominated dropping (lower bound)
for applicant in applicants.values():
    applicant.correct_dominated_dropping_lower_bound(applicant.ranking, applicant.priority_scores, dual_self_funded_program_dictionary)

# TODO: correct dominated flipping lower bound
# TODO: correct dominated choices lower bound


# refactor setting contracts, programs, applicants -> add functions with tests
# TODO: Add function that updates score dictionary and ranking in contracts:


# Initialize matching
for applicant in applicants.values():
    applicant.initialize_ranking(applicant.ranking_lower_bound, applicant.priority_scores_lower_bound)

# Add single tie-breaking
STB(applicants)

for applicant in applicants.values():
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


# Run matching
matching = student_proposing_deferred_acceptance(applicants, contracts)

from heapq import heappop, heappush
import random
from types import NoneType
from python.applicant import Applicant
from python.contract import Contract
from python.program import Program
from python.config import CAPACITY_MIN, PRIORITY_SCORE_CUTOFF_MIN, CAPACITY_FACTOR
from python.data_utils import create_applicants, create_contracts, create_programs
from python.matching_utils import add_single_tie_breaker, compute_priority_score_cutoffs_from_matching, student_proposing_deferred_acceptance, summarize_dominated_choices, verify_stability
import pandas as pd
import math

d = {
        'applicant_id': ["A1", "A1", "A1", "A2", "A2", "A2", "A3", "A3", "A3"],
        'rank': [1, 2, 3, 1, 2, 3, 1, 2, 3],
        'program_id': ["P1", "P1", "P3", "P1", "P3", "P3", "P5", "P3", "P1"],
        'contract_id': ["C1", "C2", "C4", "C1", "C4", "C2", "C5", "C3", "C1"],
        'state_funded': [True, False, False, True, False, True, True, True, True],
        'priority_score': [10, 11, 12, 13, 14, 15, 16, 17, 18],
        'capacity': [1, 1, 1, 1, 1, 1, 1, 1, 1],
    }
data = pd.DataFrame(data=d)

# Create applicants and contracts
applicants = create_applicants(data)
contracts = create_contracts(data)

# Initialize matching
for applicant in applicants.values():
    applicant.initialize_ranking(applicant.ranking, applicant.priority_scores)
add_single_tie_breaker(applicants)

# Initialize contracts
for applicant in applicants.values():
    for r in range(len(applicant.ranking_sorted)):
        contracts[applicant.ranking_sorted[r]].score_dictionary[applicant.applicant_id] = applicant.priority_scores_sorted[r]

# Compute matching
matching = student_proposing_deferred_acceptance(applicants, contracts)

# Compute priority scores
priority_score_cutoffs = compute_priority_score_cutoffs_from_matching(matching, contracts)

# Verify stability
verify_stability(matching, applicants, priority_score_cutoffs)
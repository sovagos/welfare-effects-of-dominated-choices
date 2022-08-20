from types import NoneType
import pandas as pd
from python.applicant import Applicant
from python.contract import Contract
from python.program import Program
from python.config import CAPACITY_MIN, PRIORITY_SCORE_CUTOFF_MIN, CAPACITY_FACTOR
from python.data_utils import create_applicants, create_contracts, create_programs
from python.matching_utils import summarize_dominated_choices
from python.validate_data import validate_data

d = {
        'applicant_id': ["A1", "A1", "A1", "A2", "A2", "A2", "A3", "A3", "A3"],
        'rank': [1, 2, 3, 1, 2, 3, 1, 2, 3],
        'program_id': ["P1", "P1", "P3", "P1", "P3", "P3", "P5", "P3", "P1"],
        'contract_id': ["C1", "C2", "C4", "C1", "C4", "C3", "C5", "C3", "C1"],
        'state_funded': [True, False, False, True, False, True, True, True, True],
        'priority_score': [10, 11, 12, 13, 14, 15, 16, 17, 18],
        'capacity': [1, 1, 1, 1, 1, 1, 1, 1, 1]
    }
data = pd.DataFrame(data=d)

# Validate data
validate_data(data)

# Create applicants
applicants = create_applicants(data)

# Create contracts and add capacities
contracts = create_contracts(data)

# Create programs
programs = create_programs(contracts)

# Create dual self funded dictionary
dual_self_funded_program_dictionary = {}
for program in programs.values():
    dual_self_funded_program_dictionary.update(program.create_self_funded_program_dictionary())

# Add and summarize dominated choices
for applicant in applicants.values():
    applicant.add_dominated_dropping(dual_self_funded_program_dictionary, applicant.ranking)
    applicant.add_dominated_flipping(dual_self_funded_program_dictionary, applicant.ranking)
summarize_dominated_choices(applicants)

# Test whether dominated choices are corrected
## Test whether dominated dropping are corrected
for applicant in applicants.values():
    applicant.correct_dominated_dropping_lower_bound(applicant.ranking, applicant.priority_scores, dual_self_funded_program_dictionary)
    applicant.add_dominated_dropping(dual_self_funded_program_dictionary, applicant.ranking_lower_bound)
    applicant.add_dominated_flipping(dual_self_funded_program_dictionary, applicant.ranking_lower_bound)
summarize_dominated_choices(applicants)

## Test whether dominated flipping are corrected
for applicant in applicants.values():
    applicant.correct_dominated_flipping_lower_bound(applicant.ranking, applicant.priority_scores, dual_self_funded_program_dictionary)
    applicant.add_dominated_dropping(dual_self_funded_program_dictionary, applicant.ranking_lower_bound)
    applicant.add_dominated_flipping(dual_self_funded_program_dictionary, applicant.ranking_lower_bound)
summarize_dominated_choices(applicants)

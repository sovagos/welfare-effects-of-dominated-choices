import pandas as pd
from python.applicant import Applicant
from python.contract import Contract
from python.program import Program
from python.data_utils import create_applicants, create_contracts
from python.matching_utils import add_single_tie_breaker, compute_priority_score_cutoffs_from_matching, student_proposing_deferred_acceptance, verify_stability
from python.validate_data import validate_data

def calculate(data):
    validate_data(data)
    applicants = create_applicants(data)
    contracts = create_contracts(data)
    for applicant in applicants.values():
        applicant.initialize_ranking(applicant.ranking, applicant.priority_scores)
    add_single_tie_breaker(applicants)
    for applicant in applicants.values():
        for r in range(len(applicant.ranking_sorted)):
            contracts[applicant.ranking_sorted[r]].score_dictionary[applicant.applicant_id] = applicant.priority_scores_sorted[r]
    matching = student_proposing_deferred_acceptance(applicants, contracts)
    priority_score_cutoffs = compute_priority_score_cutoffs_from_matching(matching, contracts)
    verify_stability(matching, applicants, priority_score_cutoffs)
    return priority_score_cutoffs

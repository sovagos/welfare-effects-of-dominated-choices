from python.applicant import Applicant
from python.contract import Contract
from python.program import Program
from python.data_utils import create_applicants, create_contracts, create_programs
from python.matching_utils import add_single_tie_breaker, compute_priority_score_cutoffs_from_matching, student_proposing_deferred_acceptance, summarize_dominated_choices
import pandas as pd
import math


def calculate(data):
    applicants = create_applicants(data)
    contracts = create_contracts(data)
    for applicant in applicants.values():
        applicant.initialize_ranking(applicant.ranking, applicant.priority_scores)
    add_single_tie_breaker(applicants)
    for applicant in applicants.values():
        for r in range(len(applicant.ranking_sorted)):
            contracts[applicant.ranking_sorted[r]].score_dictionary[applicant.applicant_id] = applicant.priority_scores_sorted[r]
    matching = student_proposing_deferred_acceptance(applicants, contracts)
    return compute_priority_score_cutoffs_from_matching(matching, contracts)

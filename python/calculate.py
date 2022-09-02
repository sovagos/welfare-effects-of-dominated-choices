from python.compute_priority_score_cutoffs_from_matching import (
    compute_priority_score_cutoffs_from_matching,
)
from python.data_utils import create_applicants, create_contracts
from python.floor_priority_score_cutoffs import floor_priority_score_cutoffs
from python.matching_utils import (
    add_single_tie_breaker,
    student_proposing_deferred_acceptance,
)
from python.validate_data import validate_data
from python.verify_stability import verify_stability


def calculate(data):
    validate_data(data)
    applicants = create_applicants(data)
    contracts = create_contracts(data)
    for applicant in applicants.values():
        applicant.initialize_ranking(applicant.ranking, applicant.priority_scores)
    add_single_tie_breaker(applicants)
    for applicant in applicants.values():
        for r in range(len(applicant.ranking_sorted)):
            contracts[applicant.ranking_sorted[r]].score_dictionary[
                applicant.applicant_id
            ] = applicant.priority_scores_sorted[r]
    matching = student_proposing_deferred_acceptance(applicants, contracts)
    priority_score_cutoffs = compute_priority_score_cutoffs_from_matching(
        matching, contracts
    )
    verify_stability(matching, applicants, priority_score_cutoffs)
    return floor_priority_score_cutoffs(priority_score_cutoffs)

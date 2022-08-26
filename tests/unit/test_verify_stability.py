import pytest

from python.applicant import Applicant
from python.verify_stability import verify_stability

def test__verify_stability__applicant_admitted_to_most_preferred_contract__returns_no_exception():
    # define inputs (arrange)
    matching = {"A1": "C1"}
    applicant = Applicant("A1")
    applicant.ranking_sorted = ["C1"]
    applicant.priority_scores_sorted = [1]
    applicants = {applicant.applicant_id: applicant}
    priority_score_cutoffs = {"C1": 0}

    # run function (act)
    verify_stability(matching, applicants, priority_score_cutoffs)

    # assert

def test__verify_stability__applicant_is_not_admitted_to_contract_with_low_priority_score_cutoff__returns_exception():
    matching = {"A1": None}
    applicant = Applicant("A1")
    applicant.ranking_sorted = ["C1"]
    applicant.priority_scores_sorted = [1]
    applicants = {applicant.applicant_id: applicant}
    priority_score_cutoffs = {"C1": 0}

    with pytest.raises(ValueError, match="The matching is not stable: an applicant could have been admitted to a more preferred contract"):
        verify_stability(matching, applicants, priority_score_cutoffs)


def test__verify_stability__applicant_admitted_to_second_most_preferred_contract__returns_exception():
    matching = {"A1": "C2"}
    applicant = Applicant("A1")
    ranking_priority_score = {"C1": 1, "C2": 1}
    applicant.ranking_sorted = ["C1", "C2"]
    applicant.priority_scores_sorted = [ranking_priority_score["C1"], ranking_priority_score["C2"]]
    applicants = {applicant.applicant_id: applicant}
    priority_score_cutoffs = {"C1": 0, "C2": 0}

    with pytest.raises(ValueError, match="The matching is not stable: an applicant could have been admitted to a more preferred contract"):
        verify_stability(matching, applicants, priority_score_cutoffs)


def test__verify_stability__some_applicant_is_not_admitted_to_contract_with_low_priority_score_cutoff__returns_exception():
    matching = {"A1": "C1", "A2": None}
    applicant_A1 = Applicant("A1")
    applicant_A1.ranking_sorted = ["C1"]
    applicant_A1.priority_scores_sorted = [1]
    applicant_A2 = Applicant("A2")
    applicant_A2.ranking_sorted = ["C1"]
    applicant_A2.priority_scores_sorted = [2]
    applicants = {applicant_A1.applicant_id: applicant_A1, applicant_A2.applicant_id: applicant_A2}
    priority_score_cutoffs = {"C1": 0}

    with pytest.raises(ValueError, match="The matching is not stable: an applicant could have been admitted to a more preferred contract"):
        verify_stability(matching, applicants, priority_score_cutoffs)


def test__verify_stability__applicant_is_not_admitted_to_contract_but_could_have_admitted_to_least_preferred__returns_exception():
    matching = {"A1": None}
    applicant = Applicant("A1")
    ranking_priority_score = {"C1": 1, "C2": 1}
    applicant.ranking_sorted = ["C1", "C2"]
    applicant.priority_scores_sorted = [ranking_priority_score["C1"], ranking_priority_score["C2"]]
    applicants = {applicant.applicant_id: applicant}
    priority_score_cutoffs = {"C1": 2, "C2": 0}

    with pytest.raises(ValueError, match="The matching is not stable: an applicant could have been admitted to a more preferred contract"):
        verify_stability(matching, applicants, priority_score_cutoffs)

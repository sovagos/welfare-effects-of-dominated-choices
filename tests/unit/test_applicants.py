from python.applicant import Applicant

def test_if_applicant_has_proper_applicant_id():
    applicant = Applicant(1)
    
    assert applicant.applicant_id == 1

def test_if_applicants_ranking_is_a_list():
    applicant = Applicant(1)

    assert type(applicant.ranking) is list
    assert type(applicant.priority_scores) is list

def test_when_applicant_made_a_dominated_dropping__then_add_dominated_dropping__returns_true():
    applicant = Applicant(1)
    applicant.ranking = [[1, 2]]
    dual_program_dictionary = {2:1}

    applicant.add_dominated_dropping(dual_program_dictionary)

    assert applicant.dominated_dropping == True

def test_when_applicant_made_no_dominated_dropping__then_add_dominated_dropping__returns_false():
    applicant = Applicant(1)
    applicant.ranking = [[1, 1], [2, 2]]
    dual_program_dictionary = {2:1}

    applicant.add_dominated_dropping(dual_program_dictionary)

    assert applicant.dominated_dropping == False

def test_when_applicant_made_dominated_flipping__then_add_dominated_dropping__returns_false():
    applicant = Applicant(1)
    applicant.ranking = [[1, 2], [2, 1]]
    dual_program_dictionary = {2:1}

    applicant.add_dominated_dropping(dual_program_dictionary)

    assert applicant.dominated_dropping == False

def test_when_applicant_made_a_dominated_flipping__then_add_dominated_flipping__returns_true():
    applicant = Applicant(1)
    applicant.ranking = [[1, 2], [2, 1]]
    dual_program_dictionary = {2:1}

    applicant.add_dominated_flipping(dual_program_dictionary)

    assert applicant.dominated_flipping == True

def test_when_applicant_made_no_dominated_flipping__then_add_dominated_flipping__returns_false():
    applicant = Applicant(1)
    applicant.ranking = [[1, 1], [2, 2]]
    dual_program_dictionary = {2:1}

    applicant.add_dominated_flipping(dual_program_dictionary)

    assert applicant.dominated_flipping == False

def test_when_applicant_made_dominated_dropping__then_add_dominated_flipping__returns_false():
    applicant = Applicant(1)
    applicant.ranking = [[1, 2]]
    dual_program_dictionary = {2:1}

    applicant.add_dominated_flipping(dual_program_dictionary)

    assert applicant.dominated_flipping == False

def test_when_applicant_has_a_ranking__then_correct_dominated_dropping_lower_bound__creates_ranking_lower_bound():
    applicant = Applicant(1)
    dual_program_dictionary = {2:1}

    applicant.correct_dominated_dropping_lower_bound(applicant.ranking, applicant.priority_scores, dual_program_dictionary)

    assert type(applicant.ranking_lower_bound) is list
    assert type(applicant.priority_scores_lower_bound) is list

def test_when_applicant_makes_dominated_dropping__then_correct_dominated_dropping_lower_bound__creates_correct_ranking_lower_bound():
    applicant = Applicant(1)
    applicant.ranking = [[1, 2]]
    applicant.priority_scores = [[1, 10]]
    dual_program_dictionary = {2:1}

    applicant.correct_dominated_dropping_lower_bound(applicant.ranking, applicant.priority_scores, dual_program_dictionary)

    assert applicant.ranking_lower_bound == [[0.5, 1], [1, 2]]
    assert applicant.priority_scores_lower_bound == [[0.5, 10], [1, 10]]

def test_when_applicant_makes_no_dominated_dropping__then_correct_dominated_dropping_lower_bound__creates_correct_ranking_lower_bound():
    applicant = Applicant(1)
    applicant.ranking = [[1, 1]]
    applicant.priority_scores = [[1, 10]]
    dual_program_dictionary = {2:1}

    applicant.correct_dominated_dropping_lower_bound(applicant.ranking, applicant.priority_scores, dual_program_dictionary)

    assert applicant.ranking_lower_bound == [[1, 1]]
    assert applicant.priority_scores_lower_bound == [[1, 10]]
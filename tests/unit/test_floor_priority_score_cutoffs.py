from python.floor_priority_score_cutoffs import floor_priority_score_cutoffs


def test__floor_priority_score_cutoffs__when_priority_score_cutoff_is_not_an_integer__returns_floored_value():
    priority_score_cutoffs = {"C1": 1.6}

    floored_priority_score_cutoffs = floor_priority_score_cutoffs(
        priority_score_cutoffs
    )

    assert floored_priority_score_cutoffs == {"C1": 1}


def test__floor_priority_score_cutoffs__when_priority_score_cutoff_is_an_integer__returns_floored_value():
    priority_score_cutoffs = {"C1": 1}

    floored_priority_score_cutoffs = floor_priority_score_cutoffs(
        priority_score_cutoffs
    )

    assert floored_priority_score_cutoffs == {"C1": 1}


def test__floor_priority_score_cutoffs__when_priority_score_cutoffs_are_not_integers__returns_floored_value():
    priority_score_cutoffs = {"C1": 1, "C2": 2.2}

    floored_priority_score_cutoffs = floor_priority_score_cutoffs(
        priority_score_cutoffs
    )

    assert floored_priority_score_cutoffs == {"C1": 1, "C2": 2}

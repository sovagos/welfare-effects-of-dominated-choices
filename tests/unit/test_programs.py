import pandas as pd
from python.data_utils import create_contracts, create_programs

def test_when_program_is_created__then_programs__have_the_right_length():
    d = {
        'contract_id': ["C1", "C2"],
        'program_id': ["P1", "P1"],
        'state_funded': [True, False],
        'priority_score_cutoff': [10, 5],
        'capacity': [1, 1],
    }
    data = pd.DataFrame(data=d)
    contracts = create_contracts(data)
    programs = create_programs(contracts)

    assert len(programs) == 1


def test_when_program_is_dual__then_create_self_funded_program_dictionary__returns_right_contract_ids():
    d = {
        'contract_id': ["C1", "C2", "C3", "C4"],
        'program_id': ["P1", "P1", "P2", "P3"],
        'state_funded': [True, False, True, False],
        'priority_score_cutoff': [10, 5, 14, 10],
        'capacity': [1, 1, 1, 1]
    }
    data = pd.DataFrame(data=d)
    contracts = create_contracts(data)
    programs = create_programs(contracts)

    assert programs["P1"].create_self_funded_program_dictionary() == {"C2":"C1"}
    assert programs["P2"].create_self_funded_program_dictionary() == {}
    assert programs["P3"].create_self_funded_program_dictionary() == {}

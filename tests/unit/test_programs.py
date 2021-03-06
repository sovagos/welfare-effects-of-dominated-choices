import pandas as pd
from python.data_utils import create_contracts, create_programs

def test_when_program_is_created__then_programs__have_the_right_length():
    d = {
        'contract_id': [1, 2],
        'program_id': [1, 1],
        'state_funded': [1, 0],
        'priority_score_cutoff': [10, 5],
    }
    data = pd.DataFrame(data=d)
    contracts = create_contracts(data)
    programs = create_programs(contracts)

    assert len(programs) == 1


def test_when_program_is_dual__then_create_self_funded_program_dictionary__returns_right_contract_ids():
    d = {
        'contract_id': [1, 2, 3, 4],
        'program_id': [1, 1, 2, 3],
        'state_funded': [1, 0, 1, 0],
        'priority_score_cutoff': [10, 5, 14, 10],
    }
    data = pd.DataFrame(data=d)
    contracts = create_contracts(data)
    programs = create_programs(contracts)

    assert programs[1].create_self_funded_program_dictionary() == {2:1}
    assert programs[2].create_self_funded_program_dictionary() == {}
    assert programs[3].create_self_funded_program_dictionary() == {}

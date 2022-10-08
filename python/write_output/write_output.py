from python.types import ContractWithPriorityScoreCutoff
from python.write_output.get_output_from_contracts_with_priority_score_cutoffs import (
    get_output_from_contracts_with_priority_score_cutoffs,
)
from python.write_output.write_data_to_file import write_data_to_file


def write_output(file: str, data: list[ContractWithPriorityScoreCutoff]) -> None:
    write_data_to_file(
        file=file,
        data=get_output_from_contracts_with_priority_score_cutoffs(
            contracts_with_priority_score_cutoffs=data
        ),
    )

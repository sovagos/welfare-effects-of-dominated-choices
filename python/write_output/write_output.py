from python.types import Matching
from python.write_output.get_output_from_matchings import (
    get_output_from_matchings,
)
from python.write_output.write_data_to_file import write_data_to_file


def write_output(file: str, data: list[Matching]) -> None:
    write_data_to_file(
        file=file,
        data=get_output_from_matchings(matchings=data),
    )

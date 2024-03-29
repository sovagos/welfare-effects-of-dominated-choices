from typing import Callable

from python.get_input.get_input import get_input
from python.get_matching.get_matching import get_matching
from python.types import Input
from python.output.write_output_from_matchings import write_output_from_matchings


def run_application(
    input_file: str,
    output_file: str,
    correct_dominated_choices: Callable[[Input], Input],
) -> None:
    input = correct_dominated_choices(get_input(file=input_file))
    matchings = get_matching(applicants=input.applicants, contracts=input.contracts)
    write_output_from_matchings(file=output_file, data=matchings)

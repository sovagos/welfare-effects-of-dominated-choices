from os import environ, path

from python.config import INPUT_FOLDER, OUTPUT_FOLDER
from python.correct_dominated_choices.correct_dominated_choices_upper import (
    correct_dominated_choices_upper,
)
from python.get_input.get_input import get_input
from python.output.write_output_from_input import write_output_from_input


def main(input_file: str, output_file: str) -> None:
    input = correct_dominated_choices_upper(get_input(file=input_file))
    write_output_from_input(
        file=output_file,
        data=input,
    )


def _convert_boolean(value: bool) -> str:
    return "1" if value else "0"


if __name__ == "__main__":
    input_file = environ["INPUT"]
    main(
        input_file=path.join(INPUT_FOLDER, input_file),
        output_file=path.join(OUTPUT_FOLDER, f"correct_upper_input_{input_file}"),
    )

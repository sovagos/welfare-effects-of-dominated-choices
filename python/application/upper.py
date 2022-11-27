from os import environ, path

from python.application.libs.run_application import run_application
from python.config import INPUT_FOLDER, OUTPUT_FOLDER
from python.correct_dominated_choices.correct_dominated_choices_upper import (
    correct_dominated_choices_upper,
)


def main(input_file: str, output_file: str) -> None:
    run_application(
        input_file=input_file,
        output_file=output_file,
        correct_dominated_choices=correct_dominated_choices_upper,
    )


if __name__ == "__main__":
    input_file = environ["INPUT"]
    main(
        input_file=path.join(INPUT_FOLDER, input_file),
        output_file=path.join(OUTPUT_FOLDER, f"result_upper_{input_file}"),
    )

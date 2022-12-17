from python.output.libs.get_output_from_input import get_output_from_input
from python.types import Input
from python.output.libs.write_data_to_file import write_data_to_file


def write_output_from_input(file: str, data: Input) -> None:
    write_data_to_file(
        file=file,
        data=get_output_from_input(input=data),
    )

from python.get_input.get_data_from_file import get_data_from_file
from python.get_input.get_input_from_csv import get_input_from_csv
from python.types import Input


def get_input(file: str) -> Input:
    return get_input_from_csv(csv=get_data_from_file(file=file))

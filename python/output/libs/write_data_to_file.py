from csv import writer

from python.types import Output


def write_data_to_file(file: str, data: Output) -> None:
    with open(file, "w+", newline="") as csvfile:
        output = writer(csvfile, delimiter=",")
        for row in data:
            output.writerow(row)

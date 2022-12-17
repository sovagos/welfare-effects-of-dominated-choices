from csv import writer


def write_data_to_file(file: str, data: list[list[str]]) -> None:
    with open(file, "w+", newline="") as csvfile:
        output = writer(csvfile, delimiter=",")
        for row in data:
            output.writerow(row)

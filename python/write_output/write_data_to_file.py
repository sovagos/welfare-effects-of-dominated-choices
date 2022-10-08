from csv import writer


def write_data_to_file(file: str, data: list[list[str]]) -> None:
    with open(file, "w+", newline="") as csvfile:
        spamwriter = writer(csvfile, delimiter=",")
        for row in data:
            spamwriter.writerow(row)

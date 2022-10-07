from csv import reader


def get_data_from_csv(file: str) -> list[list[str]]:
    result = []
    with open(file) as csvfile:
        for row in reader(csvfile):
            result.append(row)
    return result

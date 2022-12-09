from csv import DictReader


def get_data_from_file(file: str) -> list[dict]:
    result = []
    with open(file) as csvfile:
        reader = DictReader(csvfile)
        for row in reader:
            result.append(row)
    return result

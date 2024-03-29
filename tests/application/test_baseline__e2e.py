from tests.e2e_helpers import create_input_file, run, get_result, clear


def test__baseline() -> None:
    input_data = [
        [
            "applicant_id",
            "rank",
            "priority_score",
            "contract_id",
            "capacity",
            "state_funded",
            "program_id",
            "admitted",
        ],
        ["A1", "1", "1", "C1", "1", "0", "P1", "0"],
        ["A2", "1", "80", "C2", "19", "1", "P2", "1"],
    ]
    input_filename = create_input_file(input_data)
    output_filename = f"result_{input_filename}"

    run(input_filename=input_filename, application="python.application.baseline")

    result = get_result(output_filename=output_filename)
    assert result == [
        ["applicant_id", "contract_id", "rank"],
        ["A1", "C1", "1"],
        ["A2", "C2", "1"],
    ]

    clear(input_filename=input_filename, output_filename=output_filename)

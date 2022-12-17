from tests.e2e_helpers import create_input_file, run, get_result, clear


def test__correct_upper_input() -> None:
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
        ["A1", "1", "1", "C1", "1", "1", "P1", "0"],
        ["A1", "2", "1", "C2", "1", "0", "P2", "0"],
        ["A2", "1", "1", "C3", "1", "1", "P2", "0"],
    ]
    input_filename = create_input_file(input_data)
    output_filename = f"correct_upper_input_{input_filename}"

    run(
        input_filename=input_filename,
        application="python.application.correct_upper_input",
    )

    result = get_result(output_filename=output_filename)
    assert result == [
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
        ["A1", "1", "1", "C3", "1", "1", "P2", "0"],
        ["A1", "2", "1", "C1", "1", "1", "P1", "0"],
        ["A1", "3", "1", "C2", "1", "0", "P2", "0"],
        ["A2", "1", "1", "C3", "1", "1", "P2", "0"],
    ]

    clear(input_filename=input_filename, output_filename=output_filename)

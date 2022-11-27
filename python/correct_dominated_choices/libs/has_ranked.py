from python.types import Application


def has_ranked(ranked_applications: list[Application], contract_id: str) -> bool:
    return 0 < len(
        [
            application
            for application in ranked_applications
            if application.contract == contract_id
        ]
    )

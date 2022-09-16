from random import randint, random
from uuid import uuid4


def get_random_string() -> str:
    return str(uuid4()).replace("-", "_")


def get_random_int() -> int:
    return randint(1, 20000)


def get_random_float() -> float:
    return random()

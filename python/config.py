from os import path
from pathlib import Path

BASE_PATH = path.join(
    Path(__file__).parent.resolve(),
    "..",
)
INPUT_FOLDER = path.join(BASE_PATH, "input")
OUTPUT_FOLDER = path.join(BASE_PATH, "output")

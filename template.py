import os
from pathlib import Path


list_of_files = [
    "src/__init__.py",
    "src/data/file.csv",
    "src/exercise/exercise.sql",
    "src/requirements.txt", 
    "src/experiments/experiments.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # create an empty file





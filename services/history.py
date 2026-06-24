import json
import os

HISTORY_DIR = "data"
HISTORY_FILE = os.path.join(
    HISTORY_DIR,
    "scan_history.json"
)

def save_scan(record):

    # Create folder automatically
    os.makedirs(
        HISTORY_DIR,
        exist_ok=True
    )

    # Create file if not exists
    if not os.path.exists(HISTORY_FILE):

        with open(
            HISTORY_FILE,
            "w"
        ) as f:

            json.dump([], f)

    try:

        with open(
            HISTORY_FILE,
            "r"
        ) as f:

            data = json.load(f)

    except (json.JSONDecodeError, FileNotFoundError):

        data = []

    data.insert(
        0,
        record
    )

    with open(
        HISTORY_FILE,
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


def get_history():

    os.makedirs(
        HISTORY_DIR,
        exist_ok=True
    )

    if not os.path.exists(HISTORY_FILE):
        return []

    try:

        with open(
            HISTORY_FILE,
            "r"
        ) as f:

            return json.load(f)

    except (json.JSONDecodeError, FileNotFoundError):

        return []

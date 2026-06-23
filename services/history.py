import json
import os


HISTORY_FILE = "data/scan_history.json"


def save_scan(record):

    if not os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "w") as f:
            json.dump([], f)

    with open(HISTORY_FILE, "r") as f:
        data = json.load(f)

    data.insert(0, record)

    with open(HISTORY_FILE, "w") as f:
        json.dump(
            data,
            f,
            indent=4
        )


def get_history():

    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as f:
        return json.load(f)
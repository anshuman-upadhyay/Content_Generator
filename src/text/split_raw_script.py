import json
from pathlib import Path


RAW_PATH = Path("input/raw_script.txt")
JSON_PATH = Path("input/script.json")


def split_raw_script():
    """
    Convert raw script into title/content json
    """

    if not RAW_PATH.exists():
        raise FileNotFoundError(
            "raw_script.txt not found"
        )

    text = RAW_PATH.read_text(
        encoding="utf-8"
    ).strip()

    if not text:
        raise ValueError(
            "raw script is empty"
        )

    lines = text.split("\n")

    title = lines[0].strip()

    content = " ".join(
        line.strip()
        for line in lines[1:]
        if line.strip()
    )

    if not content:
        raise ValueError(
            "Story content missing"
        )

    data = {
        "title": title,
        "content": content
    }

    with open(
        JSON_PATH,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            data,
            f,
            indent=4
        )

    print(
        "script.json created successfully"
    )


if __name__ == "__main__":
    split_raw_script()
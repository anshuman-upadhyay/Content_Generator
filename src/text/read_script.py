from pathlib import Path
import json


SCRIPT_PATH = Path("input/script.json")


def read_script():
    """
    Reads narration content
    from script.json
    """

    if not SCRIPT_PATH.exists():
        raise FileNotFoundError(
            f"script.json not found at "
            f"{SCRIPT_PATH}"
        )

    with open(
        SCRIPT_PATH,
        "r",
        encoding="utf-8"
    ) as file:
        data = json.load(file)

    content = data.get(
        "content",
        ""
    ).strip()

    if not content:
        raise ValueError(
            "Story content is empty "
            "inside script.json"
        )

    return content


if __name__ == "__main__":
    script = read_script()

    print(
        "Narration content loaded "
        "successfully:\n"
    )

    print(script)
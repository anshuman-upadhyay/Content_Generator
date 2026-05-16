from pathlib import Path
import re
import gc
import json
import language_tool_python

from src.utils.config_reader import load_config


SCRIPT_JSON_PATH = Path("input/script.json")


def basic_cleanup(text):
    """
    Lightweight regex cleanup
    """

    # remove extra spaces/newlines
    text = re.sub(r"\s+", " ", text)

    # fix repeated punctuation
    text = re.sub(r"\?{2,}", "?", text)
    text = re.sub(r"!{2,}", "!", text)
    text = re.sub(r"\.{2,}", ".", text)
    text = re.sub(r",{2,}", ",", text)

    # capitalize first letter
    if text:
        text = text[0].upper() + text[1:]

    # capitalize after punctuation
    text = re.sub(
        r'([.!?]\s+)([a-z])',
        lambda m: (
            m.group(1) +
            m.group(2).upper()
        ),
        text
    )

    return text.strip()


def advanced_cleanup(text):
    """
    Grammar correction using LanguageTool
    """

    print(
        "Running advanced grammar correction..."
    )

    tool = language_tool_python.LanguageTool(
        "en-US"
    )

    corrected_text = tool.correct(text)

    # cleanup
    tool.close()
    del tool
    gc.collect()

    print(
        "LanguageTool cleanup completed"
    )

    return corrected_text


def clean_script():
    """
    Clean title + content separately
    inside script.json
    """

    config = load_config()

    if not SCRIPT_JSON_PATH.exists():
        raise FileNotFoundError(
            "script.json not found"
        )

    with open(
        SCRIPT_JSON_PATH,
        "r",
        encoding="utf-8"
    ) as f:
        data = json.load(f)

    title = data.get("title", "").strip()
    content = data.get("content", "").strip()

    if not title:
        raise ValueError(
            "Title missing in script.json"
        )

    if not content:
        raise ValueError(
            "Content missing in script.json"
        )

    print(
        "Running basic cleanup..."
    )

    cleaned_title = basic_cleanup(
        title
    )

    cleaned_content = basic_cleanup(
        content
    )

    if config.get(
        "use_advanced_grammar_correction",
        False
    ):
        cleaned_title = advanced_cleanup(
            cleaned_title
        )

        cleaned_content = advanced_cleanup(
            cleaned_content
        )

    cleaned_data = {
        "title": cleaned_title,
        "content": cleaned_content
    }

    with open(
        SCRIPT_JSON_PATH,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            cleaned_data,
            f,
            indent=4
        )

    print(
        f"Cleaned script saved to "
        f"{SCRIPT_JSON_PATH}"
    )


if __name__ == "__main__":
    clean_script()
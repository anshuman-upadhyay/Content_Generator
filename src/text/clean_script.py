from pathlib import Path
import re
import gc
import language_tool_python

from src.utils.config_reader import load_config


RAW_SCRIPT_PATH = Path("input/raw_script.txt")
FINAL_SCRIPT_PATH = Path("input/script.txt")


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

    # capitalize first character
    if text:
        text = text[0].upper() + text[1:]

    # capitalize after punctuation
    text = re.sub(
        r'([.!?]\s+)([a-z])',
        lambda m: m.group(1) + m.group(2).upper(),
        text
    )

    # ensure ending punctuation
    if text and text[-1] not in ".!?":
        text += "."

    return text.strip()


def advanced_cleanup(text):
    """
    Grammar correction using LanguageTool
    """

    print("Running advanced grammar correction...")

    tool = language_tool_python.LanguageTool("en-US")

    corrected_text = tool.correct(text)

    # cleanup LanguageTool process
    tool.close()
    del tool
    gc.collect()

    print("LanguageTool cleanup completed")

    return corrected_text


def clean_script():
    """
    Main script cleaning pipeline
    """

    config = load_config()

    if not RAW_SCRIPT_PATH.exists():
        raise FileNotFoundError(
            "raw_script.txt not found"
        )

    raw_text = RAW_SCRIPT_PATH.read_text(
        encoding="utf-8"
    ).strip()

    if not raw_text:
        raise ValueError(
            "raw_script.txt is empty"
        )

    print("Running basic cleanup...")

    cleaned_text = basic_cleanup(raw_text)

    if config.get(
        "use_advanced_grammar_correction",
        False
    ):
        cleaned_text = advanced_cleanup(
            cleaned_text
        )

    FINAL_SCRIPT_PATH.write_text(
        cleaned_text,
        encoding="utf-8"
    )

    print(
        f"Final cleaned script saved to "
        f"{FINAL_SCRIPT_PATH}"
    )


if __name__ == "__main__":
    clean_script()
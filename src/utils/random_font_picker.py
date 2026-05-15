from pathlib import Path
import random


FONT_FOLDER = Path("assets/fonts")


def pick_random_font():
    """
    Pick random font
    """

    if not FONT_FOLDER.exists():
        raise FileNotFoundError(
            "assets/fonts folder not found"
        )

    font_files = list(
        FONT_FOLDER.glob("*.ttf")
    )

    if not font_files:
        raise ValueError(
            "No font files found"
        )

    selected_font = random.choice(
        font_files
    )

    print(
        f"Selected font: "
        f"{selected_font.name}"
    )

    return selected_font
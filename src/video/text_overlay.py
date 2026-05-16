from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap
import subprocess
import json

from src.utils.random_font_picker import pick_random_font


SCRIPT_PATH = Path("input/script.json")
CARD_PATH = Path("temp/overlays/story_card.png")


def get_story_title():
    """
    Read only title from script.json
    """
    if not SCRIPT_PATH.exists():
        raise FileNotFoundError(
            "script.json not found"
        )

    with open(
        SCRIPT_PATH,
        "r",
        encoding="utf-8"
    ) as file:
        data = json.load(file)

    title = data.get(
        "title",
        ""
    ).strip()

    if not title:
        raise ValueError(
            "Title missing in script.json"
        )

    # truncate extreme titles
    if len(title) > 120:
        title = title[:120] + "..."

    wrapped_title = textwrap.fill(
        title,
        width=28
    )

    return wrapped_title


def create_story_card():
    """
    Create title-only story card
    """
    CARD_PATH.parent.mkdir(
        exist_ok=True
    )

    title_text = get_story_title()

    title_lines = (
        title_text.count("\n") + 1
    )

    width = 900

    # Much smaller card now
    base_height = 180
    line_height = 55

    height = (
        base_height +
        (title_lines * line_height)
    )

    image = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(image)

    # shadow
    draw.rounded_rectangle(
        [
            (20, 20),
            (width - 10, height - 10)
        ],
        radius=35,
        fill=(0, 0, 0, 180)
    )

    # main card
    draw.rounded_rectangle(
        [
            (0, 0),
            (width - 30, height - 30)
        ],
        radius=35,
        fill=(15, 15, 35, 245)
    )

    selected_font = pick_random_font()

    font_header = ImageFont.truetype(
        str(selected_font),
        46
    )

    font_title = ImageFont.truetype(
        str(selected_font),
        40
    )

    # Header
    draw.text(
        (50, 35),
        "🔥 STORY TIME",
        fill="white",
        font=font_header
    )

    # Title only
    draw.multiline_text(
        (50, 120),
        title_text,
        fill="white",
        font=font_title,
        spacing=20
    )

    image.save(CARD_PATH)

    print(
        "Title-only story card created"
    )

    return selected_font.name


def add_text_overlay(folder):
    """
    Overlay story card
    """
    input_video = (
        folder["long_folder"] /
        "final_video.mp4"
    )

    output_video = (
        folder["long_folder"] /
        "overlay_video.mp4"
    )

    if not input_video.exists():
        raise FileNotFoundError(
            "final_video.mp4 not found"
        )

    selected_font_name = create_story_card()

    command = [
        "ffmpeg",
        "-y",
        "-i", str(input_video),
        "-i", str(CARD_PATH),

        "-filter_complex",

        # upper-middle placement
        "overlay=(main_w-overlay_w)/2:350",

        "-c:a", "copy",
        str(output_video)
    ]

    subprocess.run(
        command,
        check=True
    )

    input_video.unlink()

    print(
        "Overlay video created successfully"
    )

    return selected_font_name


if __name__ == "__main__":
    print(
        "Run through pipeline"
    )
    
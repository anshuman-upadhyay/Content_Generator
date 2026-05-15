from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap
import subprocess
from src.utils.random_font_picker import pick_random_font


SCRIPT_PATH = Path("input/script.txt")
CARD_PATH = Path("temp/overlays/story_card.png")


def get_story_preview():
    """
    Extract preview text for story card
    """
    text = SCRIPT_PATH.read_text(
        encoding="utf-8"
    ).strip()

    preview = text[:110]

    wrapped = textwrap.fill(
        preview,
        width=22
    )

    return wrapped


def create_story_card():
    """
    Create story card and return selected font
    """
    CARD_PATH.parent.mkdir(
        exist_ok=True
    )

    width = 850
    height = 320

    image = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(image)

    # shadow layer
    draw.rounded_rectangle(
        [(20, 20), (width-10, height-10)],
        radius=35,
        fill=(0, 0, 0, 120)
    )

    # main card
    draw.rounded_rectangle(
        [(0, 0), (width-30, height-30)],
        radius=35,
        fill=(15, 15, 35, 245)
    )

    # random font selection
    selected_font = pick_random_font()

    font_title = ImageFont.truetype(
        str(selected_font),
        58
    )

    font_body = ImageFont.truetype(
        str(selected_font),
        44
    )

    preview = get_story_preview()

    if len(preview) > 170:
        preview = preview[:170] + "....."

    preview = textwrap.fill(
        preview,
        width=28
    )

    draw.text(
        (50, 35),
        "STORY TIME",
        fill="white",
        font=font_title
    )

    draw.text(
        (50, 125),
        preview,
        fill=(230, 230, 230),
        font=font_body
    )

    image.save(CARD_PATH)

    print("Improved story card created")

    # return font for metadata logging
    return selected_font.name


def add_text_overlay(folder):
    """
    Overlay story card onto final video
    and return selected font
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

    # capture selected font
    selected_font_name = create_story_card()

    command = [
        "ffmpeg",
        "-y",
        "-i", str(input_video),
        "-i", str(CARD_PATH),

        "-filter_complex",
        "overlay=(main_w-overlay_w)/2:650",

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
        "Run this through pipeline"
    )
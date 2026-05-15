from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap
import subprocess


SCRIPT_PATH = Path("input/script.txt")
CARD_PATH = Path("temp/overlays/story_card.png")


def get_story_preview():
    """
    Extract shorter preview text for cleaner overlay
    """
    text = SCRIPT_PATH.read_text(
        encoding="utf-8"
    ).strip()

    # shorter preview so box doesn't become overcrowded
    preview = text[:110]

    # tighter wrapping for better readability
    wrapped = textwrap.fill(
        preview,
        width=22
    )

    return wrapped

def create_story_card():
    CARD_PATH.parent.mkdir(exist_ok=True)

    width = 850
    height = 320

    # transparent base canvas
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

    # main card layer
    draw.rounded_rectangle(
        [(0, 0), (width-30, height-30)],
        radius=35,
        fill=(15, 15, 35, 245)
    )

    font_title = ImageFont.truetype(
        "assets/fonts/arial.ttf",
        58
    )

    font_body = ImageFont.truetype(
        "assets/fonts/arial.ttf",
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

def add_text_overlay(folder):
    """
    Overlay story card onto final video
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

    create_story_card()

    command = [
        "ffmpeg",
        "-y",

        "-i", str(input_video),
        "-i", str(CARD_PATH),

        "-filter_complex",

        # moved lower → directly above subtitles
        "overlay=(main_w-overlay_w)/2:650",

        "-c:a", "copy",

        str(output_video)
    ]

    subprocess.run(
        command,
        check=True
    )

    # remove old video after overlay
    input_video.unlink()

    print("Overlay video created successfully")


if __name__ == "__main__":
    print(
        "Run this through pipeline"
    )
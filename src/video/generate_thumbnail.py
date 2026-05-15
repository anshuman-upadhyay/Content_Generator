from pathlib import Path
import textwrap
from PIL import Image, ImageDraw, ImageFont


SCRIPT_PATH = Path("input/script.txt")


def get_thumbnail_text():
    """
    Extract thumbnail hook text
    """
    text = SCRIPT_PATH.read_text(
        encoding="utf-8"
    ).strip()

    preview = text[:80] + "..."

    wrapped = textwrap.fill(
        preview,
        width=18
    )

    return wrapped


def generate_thumbnail(folder):
    """
    Create simple thumbnail
    """

    width = 1280
    height = 720

    image = Image.new(
        "RGB",
        (width, height),
        (20, 20, 40)
    )

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(
        "assets/fonts/arial.ttf",
        80
    )

    hook_text = get_thumbnail_text()

    draw.text(
        (100, 200),
        "STORY TIME",
        fill="white",
        font=font
    )

    draw.text(
        (100, 320),
        hook_text,
        fill=(255, 200, 0),
        font=font
    )

    output_path = (
        folder["run_folder"] /
        "thumbnail.png"
    )

    image.save(output_path)

    print(
        f"Thumbnail saved at "
        f"{output_path}"
    )
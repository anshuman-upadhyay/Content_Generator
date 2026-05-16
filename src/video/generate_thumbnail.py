from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap
import json


SCRIPT_PATH = Path("input/script.json")
BACKGROUND_PATH = Path(
    "assets/backgrounds/thumbnail_bg.jpg"
)


def get_thumbnail_title():
    """
    Read title from script.json
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

    if len(title) > 100:
        title = title[:100] + "..."

    wrapped_title = textwrap.fill(
        title,
        width=20
    )

    return wrapped_title


def generate_long_thumbnail(folder):
    """
    Generate long-form thumbnail
    """
    create_thumbnail(
        folder=folder,
        label="FULL STORY",
        filename="thumbnail_long.png"
    )


def generate_short_thumbnails(folder):
    """
    Generate thumbnails for shorts
    """
    shorts_folder = folder["shorts_folder"]

    short_files = sorted(
        shorts_folder.glob("*.mp4")
    )

    for i, _ in enumerate(short_files):
        create_thumbnail(
            folder=folder,
            label=f"PART {i+1}",
            filename=f"thumbnail_part_{i+1}.png"
        )


def create_thumbnail(folder, label, filename):
    """
    Create premium vertical thumbnail
    """

    width = 1080
    height = 1920

    if not BACKGROUND_PATH.exists():
        raise FileNotFoundError(
            "thumbnail background image not found"
        )

    # use your exact reference background
    image = Image.open(
        BACKGROUND_PATH
    ).convert("RGB")

    image = image.resize(
        (width, height)
    )

    draw = ImageDraw.Draw(image)

    title_text = get_thumbnail_title()

    title_font = ImageFont.truetype(
        "assets/fonts/Poppins-Bold.ttf",
        85
    )

    label_font = ImageFont.truetype(
        "assets/fonts/Poppins-Bold.ttf",
        60
    )

    # dynamic text measurement
    bbox = draw.multiline_textbbox(
        (0, 0),
        title_text,
        font=title_font,
        spacing=20
    )

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # dynamic padding
    padding_x = 160
    padding_y = 120

    box_width = text_width + padding_x
    box_height = text_height + padding_y

    # safety cap for absurd titles
    max_box_width = 900

    if box_width > max_box_width:
        box_width = max_box_width

    box_x1 = (
        width - box_width
    ) // 2

    box_y1 = (
        height - box_height
    ) // 2 - 200

    box_x2 = box_x1 + box_width
    box_y2 = box_y1 + box_height

    # stronger shadow
    draw.rounded_rectangle(
        [
            (box_x1 + 20, box_y1 + 20),
            (box_x2 + 20, box_y2 + 20)
        ],
        radius=60,
        fill=(0, 0, 0, 120)
    )

    # white card
    draw.rounded_rectangle(
        [
            (box_x1, box_y1),
            (box_x2, box_y2)
        ],
        radius=60,
        fill="white"
    )

    # center text dynamically
    text_x = box_x1 + (
        (box_width - text_width)
        // 2
    )

    text_y = box_y1 + (
        (box_height - text_height)
        // 2
    )

    draw.multiline_text(
        (
            text_x,
            text_y
        ),
        title_text,
        fill=(20, 20, 20),
        font=title_font,
        spacing=20
    )

    # label
    label_bbox = draw.textbbox(
        (0, 0),
        label,
        font=label_font
    )

    label_width = (
        label_bbox[2] -
        label_bbox[0]
    )

    draw.text(
        (
            (width - label_width) // 2,
            box_y2 + 120
        ),
        label,
        fill="white",
        font=label_font
    )

    output_path = (
        folder["run_folder"] /
        filename
    )

    image.save(output_path)

    print(
        f"Thumbnail saved: "
        f"{output_path}"
    )


def generate_thumbnail(folder):
    """
    Generate all thumbnails
    """
    generate_long_thumbnail(folder)
    generate_short_thumbnails(folder)


if __name__ == "__main__":
    print(
        "Run through pipeline"
    )
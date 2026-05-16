from pathlib import Path
import subprocess
from src.utils.random_font_picker import pick_random_font


SUBTITLE_PATH = Path("temp/subtitles.srt")


def burn_subtitles(folder):
    """
    Burn subtitles into final video
    """

    video_path = (
        folder["long_folder"] /
        "overlay_video.mp4"
    )

    output_path = (
        folder["long_folder"] /
        "Finalize_work.mp4"
    )

    if not video_path.exists():
        raise FileNotFoundError(
            "Overlay video not found"
        )

    if not SUBTITLE_PATH.exists():
        raise FileNotFoundError(
            "Subtitle file not found"
        )

    # Random subtitle font
    selected_font = pick_random_font()
    font_name = selected_font.stem

    # Prevent ugly fonts in subtitles
    banned_fonts = [
        "ArianaVioleta",
        "HappySwirly",
        "CookieCrisp",
        "ShinyCrystal",
        "BrownieStencil",
        "ShadeBlue",
        "04B"
    ]

    for bad_font in banned_fonts:
        if bad_font.lower() in font_name.lower():
            print(
                f"{font_name} skipped for subtitles "
                f"(unreadable)"
            )

            font_name = "Arial"
            break

    print(
        f"Subtitle font selected: {font_name}"
    )

    subtitle_style = (
        f"FontName={font_name},"
        "Fontsize=12,"
        "PrimaryColour=&HFFFFFF&,"
        "OutlineColour=&H000000&,"
        "BorderStyle=1,"
        "Outline=3,"
        "Shadow=2,"
        "Bold=1,"
        "Alignment=2,"

        # moved lower to avoid card collision
        "MarginV=80"
                )

    command = [
        "ffmpeg",
        "-y",
        "-threads", "2",
        "-i", str(video_path),

        "-vf",
        (
            f"subtitles={SUBTITLE_PATH}:"
            f"force_style='{subtitle_style}'"
        ),

        "-c:a", "copy",
        str(output_path)
    ]

    subprocess.run(
        command,
        check=True
    )

    # cleanup previous file
    video_path.unlink()

    print(
        f"Final subtitle video saved at "
        f"{output_path}"
    )


if __name__ == "__main__":
    print("Burning subtitles")
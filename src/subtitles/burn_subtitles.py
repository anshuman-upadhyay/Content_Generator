from pathlib import Path
import subprocess

SUBTITLE_PATH = Path("temp/subtitles.srt")

def burn_subtitles(folder):
    """
    Burn subtitles in center of vertical video
    """
    video_path = folder["long_folder"]/"overlay_video.mp4"
    output_path = folder["long_folder"]/"Finalize_work.mp4"

    if not video_path.exists():
        raise FileNotFoundError("Final video not found")

    if not SUBTITLE_PATH.exists():
        raise FileNotFoundError("Subtitle file not found")

    subtitle_style = (
        "Fontsize=12,"
        "PrimaryColour=&HFFFFFF&,"
        "OutlineColour=&H000000&,"
        "BorderStyle=1,"
        "Outline=2,"
        "Shadow=1,"
        "Alignment=2,"
        "MarginV=100"
    )

    command = [
        "ffmpeg",
        "-y",
        "-threads","2",
        "-i", str(video_path),

        "-vf",
        f"subtitles={SUBTITLE_PATH}:force_style='{subtitle_style}'",

        "-c:a", "copy",
        str(output_path)
    ]

    subprocess.run(command, check=True)

    #delete original non subtitle version
    video_path.unlink()

    print(f"Final subtitle video saved at {output_path}")


if __name__ == "__main__":
    print("Buring Subtitles")
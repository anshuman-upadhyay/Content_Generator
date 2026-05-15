from pathlib import Path
from faster_whisper import WhisperModel
import gc


AUDIO_PATH = Path("temp/final_audio.mp3")
OUTPUT_PATH = Path("temp/subtitles.srt")


def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)

    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


def generate_faster_subtitles():
    """
    Generate subtitles using Faster Whisper
    """

    if not AUDIO_PATH.exists():
        raise FileNotFoundError(
            "Final audio not found"
        )

    try:
        print("Loading Faster Whisper model...")

        model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8",
            cpu_threads=2
        )

        print("Generating subtitles...")

        segments, info = model.transcribe(
            str(AUDIO_PATH),
            beam_size=3,
            language= "en"
        )

        OUTPUT_PATH.parent.mkdir(exist_ok=True)

        with open(
            OUTPUT_PATH,
            "w",
            encoding="utf-8"
        ) as f:

            for i, segment in enumerate(
                segments,
                start=1
            ):
                f.write(f"{i}\n")
                f.write(
                    f"{format_time(segment.start)} --> "
                    f"{format_time(segment.end)}\n"
                )
                f.write(
                    f"{segment.text.strip()}\n\n"
                )

        print(
            f"Subtitles saved at {OUTPUT_PATH}"
        )

        # cleanup memory
        del model
        gc.collect()

        print(
            "Faster Whisper memory cleaned successfully."
        )

    except Exception as e:
        raise RuntimeError(
            f"Subtitle generation failed: {e}"
        )


if __name__ == "__main__":
    print("Run this through content pipeline")
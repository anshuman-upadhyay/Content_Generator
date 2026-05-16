import time
from pathlib import Path

# Text
from src.text.read_script import read_script
from src.text.split_raw_script import split_raw_script
from src.text.clean_script import clean_script
from src.text.validate_script import validate_script

# Audio
from src.audio.kokoro_tts import generate_kokoro_tts
from src.audio.music_mixer import mix_audio

# Video
from src.video.random_video_picker import pick_random_video
from src.video.clip_extractor import extract_random_clip
from src.video.merge_audio_video import merge_audio_video
from src.video.text_overlay import add_text_overlay
from src.video.split_shorts import split_video
from src.video.generate_thumbnail import generate_thumbnail

# Subtitles
from src.subtitles.generate_faster_subtitles import (
    generate_faster_subtitles
)
from src.subtitles.burn_subtitles import burn_subtitles

# Utils
from src.utils.file_manager import create_run_folder
from src.utils.cleanup import cleanup_temp_file
from src.utils.logger import save_metadata


COOLDOWN_TIME = 5


def cooldown():
    """
    Prevent laptop overheating/crashes
    """
    print(f"Cooling system for {COOLDOWN_TIME} seconds...\n")
    time.sleep(COOLDOWN_TIME)


def run_step(step_name, function, *args):
    """
    Standardized step runner
    """
    print(f"\n{'='*50}")
    print(f"{step_name}")
    print(f"{'='*50}")

    result = function(*args)

    return result


def clear_processed_script():
    """
    Clear processed script after pipeline success
    """
    script_path = Path("input/script.txt")

    if script_path.exists():
        script_path.write_text("")
        print("Processed script cleared")


def run_pipeline():
    folder = None
    current_step = "Initialization"

    try:
        # --------------------------
        # TEXT PROCESSING
        # --------------------------
        current_step = "Splitting Raw Script"
        run_step(
            current_step,
            split_raw_script
        )
        current_step = "Cleaning Script"
        run_step(current_step, clean_script)
        cooldown()

        current_step = "Reading Script"
        script = run_step(current_step, read_script)

        current_step = "Validating Script"
        run_step(current_step, validate_script, script)

        # Create folders ONLY after validation passes
        current_step = "Creating Output Folder"
        folder = run_step(current_step, create_run_folder)

        # --------------------------
        # AUDIO PROCESSING
        # --------------------------
        current_step = "Generating Narration"
        selected_voice = run_step(
            current_step,
            generate_kokoro_tts,
            script
        )
        cooldown()

        current_step = "Mixing Background Music"
        run_step(current_step, mix_audio)

        # --------------------------
        # VIDEO PROCESSING
        # --------------------------
        current_step = "Picking Gameplay Video"
        selected_video = run_step(
            current_step,
            pick_random_video
        )

        current_step = "Extracting Random Clip"
        run_step(
            current_step,
            extract_random_clip,
            selected_video
        )

        current_step = "Merging Audio + Video"
        run_step(
            current_step,
            merge_audio_video,
            folder
        )
        cooldown()

        current_step = "Adding Story Overlay"
        selected_font = run_step(
            current_step,
            add_text_overlay,
            folder
        )

        cooldown()

        # --------------------------
        # SUBTITLE PROCESSING
        # --------------------------
        current_step = "Generating Subtitles"
        run_step(
            current_step,
            generate_faster_subtitles
        )
        cooldown()

        current_step = "Burning Subtitles"
        run_step(
            current_step,
            burn_subtitles,
            folder
        )
        cooldown()

        # --------------------------
        # SHORTS CREATION
        # --------------------------
        current_step = "Splitting Shorts"
        run_step(
            current_step,
            split_video,
            folder
        )

        # --------------------------
        # METADATA LOGGING
        # --------------------------
        current_step = "Saving Metadata"

        metadata = {
            "script_words": len(script.split()),
            "gameplay_used": selected_video.name,
            "font_used": selected_font,
            "voice_used": selected_voice
        }

        run_step(
            current_step,
            save_metadata,
            folder,
            metadata
        )

        # --------------------------
        # THUMBNAIL GENERATION
        # --------------------------
        current_step = "Generating Thumbnail"
        
        run_step(
            current_step,
            generate_thumbnail,
            folder
        )





        # --------------------------
        # CLEANUP
        # --------------------------
        current_step = "Cleaning Temp Files"
        run_step(
            current_step,
            cleanup_temp_file
        )

        current_step = "Clearing Script"
        run_step(
            current_step,
            clear_processed_script
        )

        print("\nPipeline completed successfully!")

    except Exception as e:
        print(f"\nPipeline failed during: {current_step}")
        print(f"Error: {e}")

        if folder:
            print(
                f"\nPartial files saved at:\n"
                f"{folder['run_folder']}"
            )

        cleanup_temp_file()


if __name__ == "__main__":
    run_pipeline()
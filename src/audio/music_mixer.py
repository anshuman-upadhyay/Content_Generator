from pathlib import Path
from pydub import AudioSegment
from src.audio.random_music_picker import pick_random_music


NARRATION_PATH = Path("temp/narration.wav")
OUTPUT_PATH = Path("temp/final_audio.mp3")


def mix_audio():
    """
    Mix narration audio with randomly selected background music
    """

    if not NARRATION_PATH.exists():
        raise FileExistsError(
            "Narration audio not found"
        )

    # pick random music track
    music_path = pick_random_music()

    if not music_path.exists():
        raise FileExistsError(
            "Background music not found"
        )

    narration = AudioSegment.from_file(
        NARRATION_PATH
    )

    music = AudioSegment.from_file(
        music_path
    )

    # lower background volume
    music = music - 25

    # loop music if shorter than narration
    while len(music) < len(narration):
        music += music

    # trim to narration length
    music = music[:len(narration)]

    # overlay narration on top
    final_audio = music.overlay(
        narration
    )

    final_audio.export(
        OUTPUT_PATH,
        format="mp3"
    )

    print(
        f"Final mixed audio saved at "
        f"{OUTPUT_PATH}"
    )


if __name__ == "__main__":
    mix_audio()
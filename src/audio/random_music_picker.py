from pathlib import Path
import random


MUSIC_FOLDER = Path("assets/music")


def pick_random_music():
    """
    Pick random background music track
    """

    if not MUSIC_FOLDER.exists():
        raise FileNotFoundError(
            "assets/music folder not found"
        )

    music_files = list(
        MUSIC_FOLDER.glob("*.mp3")
    )

    if not music_files:
        raise ValueError(
            "No music files found"
        )

    selected_music = random.choice(
        music_files
    )

    print(
        f"Selected music: "
        f"{selected_music.name}"
    )

    return selected_music


if __name__ == "__main__":
    pick_random_music()
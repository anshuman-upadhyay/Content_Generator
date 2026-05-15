from pathlib import Path
from pydub import AudioSegment

NARRATION_PATH = Path("temp/narration.wav")
MUSIC_PATH  = Path("assets/music.mp3")
OUTPUT_PATH = Path("temp/final_audio.mp3")

def mix_audio():
    """
    Mix narration audio with background music
    """
    if not NARRATION_PATH.exists():
        raise FileExistsError("Narration audio not found")
    if not MUSIC_PATH.exists():
        raise FileExistsError("Background audio not found")
    
    narration = AudioSegment.from_file(NARRATION_PATH)
    music = AudioSegment.from_file(MUSIC_PATH)

    #lower the background music volume
    music = music - 25

    #loop music if its shorter than narration
    while len(music) < len(narration) :
        music +=music
    
    #Trim music to narration length
    music = music[:len(narration)]

    #overlay narration on top of music
    final_audio=  music.overlay(narration)

    final_audio.export(
        OUTPUT_PATH,
        format = "mp3"
    )

    print(f"Final mixed audio saved at {OUTPUT_PATH}")


if __name__ == "__main__":
    mix_audio()
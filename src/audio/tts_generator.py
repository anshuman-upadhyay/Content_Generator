from gtts import gTTS #google text to speech
from pathlib import Path

OUTPUT_PATH = Path("temp/narration.mp3")

def generate_tts(script_text):
    """
    Converts text into speech and saves it as narration.mp3
    """

    if not script_text.strip():
        raise ValueError("Script text is Empty")
    
    tts = gTTS(
        text = script_text,
        lang = "en",
        slow= False
    )
    tts.save(OUTPUT_PATH)

    print(f"Narration saved Successfully at {OUTPUT_PATH}")

if __name__== "__main__":
    sample_text = "Testing Narration will be replaced with the output of read_script.py"
    generate_tts(sample_text)


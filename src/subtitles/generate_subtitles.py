from pathlib import Path
import whisper

AUDIO_PATH = Path("temp/final_audio.mp3")
OUTPUT_PATH = Path("temp/subtitles.srt")

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds %3600)// 60)
    secs = int(seconds%60)
    milliseconds = int((seconds%1) * 1000 ) 

    return f"{hours:02}:{minutes :02}:{secs:02},{milliseconds:03}"

def generate_subtitles():
    if not AUDIO_PATH.exists():
        raise FileNotFoundError("Final audio file not found")
    
    print("Loading Whisper model")
    model = whisper.load_model("base")

    print("Transcribing audio...")
    result = model.transcribe(str(AUDIO_PATH))

    segments = result["segments"]
    with open(OUTPUT_PATH ,"w",encoding= "utf-8") as f :
        for i , seg in enumerate(segments,start=1):
            start = format_timestamp(seg["start"])
            end = format_timestamp(seg["end"])
            text = seg["text"].strip()

            f.write(f"{i}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{text}\n\n")

    print(f"Subtitles saved at {OUTPUT_PATH}")

if __name__=="__main__":
    generate_subtitles()







import random
import subprocess
from pathlib import Path
from moviepy import VideoFileClip,AudioFileClip

AUDIO_PATH = Path("temp/final_audio.mp3")
OUTPUT_PATH = Path("temp/clipped_video.mp4")

def extract_random_clip(video_path):
    if not Path(video_path).exists():
        raise FileNotFoundError("Selected video not found")
    
    if not AUDIO_PATH.exists():
        raise FileNotFoundError("Final audio file not found")
    
    video = VideoFileClip(str(video_path))
    audio = AudioFileClip(str(AUDIO_PATH))
    
    video_duration = video.duration
    audio_duration = audio.duration

    print(f"Video duration : {video_duration:.2f} sec")
    print(f"Audio duration : {audio_duration:.2f} sec")

    if audio_duration > video_duration :
        raise ValueError("Audio longer than video")
    max_start = video_duration - audio_duration
    start_time = random.uniform(0,max_start)

    print(f"Random Start Time : {start_time :.2f}")

    command = [
        "ffmpeg",
        "-y",
        "-threads","2",
        "-ss",str(start_time),
        "-i",str(video_path),
        "-t", str(audio_duration),
        "-c:v","libx264",
        "-an",
        str(OUTPUT_PATH)
    ]
    subprocess.run(command,check=True)

    video.close()
    audio.close()

    print(f"Clipped Video saved at : {OUTPUT_PATH}")

if __name__ == "__main__" :
    test_video = "raw_videos/1.mp4"
    extract_random_clip(test_video)



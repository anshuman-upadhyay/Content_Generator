from pathlib import Path
import subprocess

VIDEO_PATH = Path("temp/clipped_video.mp4")
AUDIO_PATH = Path("temp/final_audio.mp3")


def merge_audio_video(folder):
    """
    Convert the horizontal gameplay to veritcal
    Merge final audio with clipped video
    """

    output_path = folder["long_folder"]/"final_video.mp4"

    if not VIDEO_PATH.exists():
        raise FileNotFoundError("Clipped Video Not Found")
    if not AUDIO_PATH.exists():
        raise FileNotFoundError("Final Audio Not Found")
    command = [
        "ffmpeg",
        "-y" ,
        "-threads","2",
        #input video
        "-i", str(VIDEO_PATH),
        #input audio
        "-i", str(AUDIO_PATH),
        #crop horizontal video -> vertical center crop
        "-vf",
        "crop = 405:720:437:0,scale  = 1080:1920",
        #encode video
        "-c:v", "libx264",
        #encode audio
        "-c:a","aac",
        #stop when shortest stream ends
        "-shortest",
        str(output_path)
    ]

    subprocess.run(command,check = True)

    print(f"Vertical Final Video saved at {output_path}")
   

if __name__=="__main__":
    print("Merging")
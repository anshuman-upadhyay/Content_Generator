from pathlib import Path
import subprocess 
import math


CHUNK_DURATION = 90 #seconds

def get_video_duration(video_path) :
    """
    Get total duration of final video using ffprobe
    """
    command = [
        "ffprobe",
        "-v", "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        str(video_path)

    ]
    result = subprocess.run(
        command,
        capture_output=True,
        text = True,
        check = True
    )
    return float(result.stdout.strip())

def split_video(folder):
    "split the long final video"

    video_path = folder["long_folder"]/"Finalize_work.mp4"
    shorts_folder = folder["shorts_folder"]

    if not video_path.exists():
        raise FileNotFoundError(
            "Final video with subtitles not found"
        )
    
    duration  = get_video_duration(video_path)
    total_parts = math.ceil(duration / CHUNK_DURATION)

    print(f"Total Video Duration :{duration :2f} seconds")
    print(f"Creating {total_parts} shorts")

    for i in range(total_parts) :
        start_time =i * CHUNK_DURATION
        remaining_duration = duration - start_time

        clip_duration = min(
            CHUNK_DURATION,
            remaining_duration

        )

        output_file = (
            shorts_folder / 
            f"short_{i+1}.mp4"
        )

        command = [
            "ffmpeg",
            "-y",
            "-i", str(video_path),
            "-ss",str(start_time),
            "-t",str(clip_duration),

            "-c","copy",
            str(output_file)
        ]

        subprocess.run(
            command,
            check=True

        )
        print(f"Created : {output_file.name}"
              f"({clip_duration :.2f} sec)")
        
        print("\nAll shorts created Successfully")

if __name__=="__main__":
    print("Splitting Video")
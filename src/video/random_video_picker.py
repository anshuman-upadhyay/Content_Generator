import random
from pathlib import Path

VIDEO_FOLDER = Path("raw_videos")

def pick_random_video():
    """
    Randomly selects a video from raw_videos folder
    """
    if not VIDEO_FOLDER.exists():
        raise FileNotFoundError("Raw_videos folder not found")
    
    video_file = list(VIDEO_FOLDER.glob("*.mp4"))
    if not video_file :
        raise ValueError("NO mp4 videos found in raw_vidoes folder")
    
    selected_video = random.choice(video_file)
    print(f"Selected video : {selected_video.name}")
    return selected_video

if __name__=="__main__":
    pick_random_video()

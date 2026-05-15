
import time
#Paths
from pathlib import Path
#get the texts
from src.text.read_script import read_script
from src.text.clean_script import clean_script
# Audio arrangements
# from src.audio.tts_generator import generate_tts
from src.audio.kokoro_tts import generate_kokoro_tts
from src.audio.music_mixer import mix_audio
#Video arrangement
from src.video.random_video_picker import pick_random_video
from src.video.clip_extractor import extract_random_clip
from src.video.merge_audio_video import merge_audio_video
from src.video.text_overlay import add_text_overlay
#subtitles 
# from src.subtitles.generate_subtitles import generate_subtitles
from src.subtitles.generate_faster_subtitles import generate_faster_subtitles
from src.subtitles.burn_subtitles import burn_subtitles 
#shorts maker
from src.video.split_shorts import split_video

#folder structure
from src.utils.file_manager import create_run_folder

#cleanup
from src.utils.cleanup import cleanup_temp_file



def run_pipeline():
    current_step = "Initialization"
    folder = None
    try :
        current_step = "Creating OutPut Folder"
        folder = create_run_folder()
        
        current_step= "Cleaning raw Script"
        print(current_step)
        clean_script()
        print("Cooling system after script generation")
        time.sleep(5)

        current_step = "Reading Script"        
        print(current_step)
        script = read_script()
        
        current_step = "Generating Narration"
        print(current_step)
        generate_kokoro_tts(script) #using kokoro
        # generate_tts(script) #using gtts

        print("Cooling system after TTS")
        time.sleep(5)
        
        current_step = "Mixing background music"
        print(current_step)
        mix_audio()
        
        current_step = "Picking Random gameplay video"
        print(current_step)
        selected_video = pick_random_video()
        
        current_step = "Extracting random clip"
        print(current_step)
        extract_random_clip(selected_video)
        
        current_step = "Merging audio + vertical video..."
        print(current_step)
        merge_audio_video(folder)

        print("Cooling system after video merge")
        time.sleep(5)

        current_step = "Adding story overlay..."
        print(current_step)
        add_text_overlay(folder)

        print("Cooling system after video overlay")
        time.sleep(5)

        
        current_step = "Generating subtitles..."
        print(current_step)
        generate_faster_subtitles() #whisper Faster
        # generate_subtitles() # Whisper

        print("Cooling system after subtitle generation")
        time.sleep(5)

        
        current_step = "Burning subtitles.."
        print(current_step)
        burn_subtitles(folder)

        print("Cooling after subtitle burning")
        time.sleep(5)
        
        current_step = "Splitting into shorts..."
        print(current_step)
        split_video(folder)

        
        current_step = "Cleaning Temporary Files"
        print(current_step)
        cleanup_temp_file()
        
        current_step = "Clearing old Script"
        print(current_step)
        Path("input/script.txt").write_text("")

        print("\nPipeline completed successfully!")
    except Exception as e :
        print(f"\nPipeline failed during : {current_step}")
        print(f"Error: {e}")
        if  folder:
            print(
                f"Partial generated files are here: \n "
                f"{folder['run_folder']}"
                )
        if Path("temp").exists():
            cleanup_temp_file()

            



        

    


from pathlib import Path
from datetime import datetime

OUTPUT_FOLDER = Path("output")

def create_run_folder():
    """
    Creates a unique folder for each pipline run
    """
    OUTPUT_FOLDER.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")


    run_folder = OUTPUT_FOLDER/f"run_{timestamp}"
    long_folder = run_folder/"long"
    shorts_folder = run_folder/"shorts"

    long_folder.mkdir(parents=True,exist_ok=True)
    shorts_folder.mkdir(parents=True,exist_ok=True)

    return{
        "run_folder" : run_folder,
        "long_folder" : long_folder,
        "shorts_folder" : shorts_folder
    }
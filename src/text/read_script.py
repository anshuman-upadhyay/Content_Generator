from pathlib import Path
SCRIPT_PATH = Path("input/script.txt") # take the input script

def read_script():
    """
    Reads the scripts text from input/script.txt
    """
    if not SCRIPT_PATH.exists():
        raise FileExistsError(
            f"Script File Not found at {SCRIPT_PATH}"
        )
    
    with open(SCRIPT_PATH,"r",encoding="utf-8") as file :
        content = file.read().strip()

    if not content :
        raise ValueError("Script.txt is empty .Please add narration text")
    
    return content


if __name__== "__main__":
    script= read_script()
    print("Script Loaded Success : \n")
    print(script)
    
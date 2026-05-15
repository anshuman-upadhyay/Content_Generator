import json
from pathlib import Path

CONFIG_PATH = Path("input/config.json")

def load_config():
    """
    Load the project configration
    """
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            "Config.json not found in input folder"
        )
    try :
        with open(CONFIG_PATH,"r") as file:
            config = json.load(file)
        return config
    except: 
        raise ValueError(
            "Invalid JSON format in config.json"
        )
    
if  __name__ == "__main__":
    config = load_config()
    print(config)
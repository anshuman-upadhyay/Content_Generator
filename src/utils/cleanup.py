from pathlib import Path

TEMP_FOLDER = Path("temp")

def cleanup_temp_file():
    """
    Delete all temporary generated Files
    after pipeline finishes
    """
    if not TEMP_FOLDER.exists():
        print("Temp Folder not found")
        return 
    
    delete_count = 0
    for file in TEMP_FOLDER.iterdir():
        if file.is_file():
            file.unlink()
            delete_count+=1
            print(f"Deleted : {file.name}")

    print(f"Cleanup completed .\n Remove {delete_count} Temporary files")
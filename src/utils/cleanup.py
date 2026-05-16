from pathlib import Path
import shutil


TEMP_FOLDER = Path("temp")

RAW_SCRIPT_PATH = Path(
    "input/raw_script.txt"
)

SCRIPT_JSON_PATH = Path(
    "input/script.json"
)


def cleanup_temp_file():
    """
    Delete all temporary generated files
    after pipeline finishes
    """

    delete_count = 0

    # -----------------------------
    # Delete temp folder contents
    # -----------------------------
    if TEMP_FOLDER.exists():

        for item in TEMP_FOLDER.iterdir():

            try:
                if item.is_file():
                    item.unlink()
                    delete_count += 1

                    print(
                        f"Deleted: {item.name}"
                    )

                elif item.is_dir():
                    shutil.rmtree(item)

                    delete_count += 1

                    print(
                        f"Deleted folder: "
                        f"{item.name}"
                    )

            except Exception as e:
                print(
                    f"Failed deleting "
                    f"{item}: {e}"
                )

    else:
        print(
            "Temp folder not found"
        )

    # -----------------------------
    # Delete script.json
    # -----------------------------
    if SCRIPT_JSON_PATH.exists():
        try:
            SCRIPT_JSON_PATH.unlink()

            delete_count += 1

            print(
                "Deleted: script.json"
            )

        except Exception as e:
            print(
                f"Failed deleting "
                f"script.json: {e}"
            )

    # -----------------------------
    # Clear raw_script.txt
    # -----------------------------
    if RAW_SCRIPT_PATH.exists():
        try:
            RAW_SCRIPT_PATH.write_text(
                "",
                encoding="utf-8"
            )

            print(
                "Cleared raw_script.txt"
            )

        except Exception as e:
            print(
                f"Failed clearing "
                f"raw_script.txt: {e}"
            )

    print(
        f"\nCleanup completed."
    )

    print(
        f"Removed {delete_count} "
        f"temporary items"
    )


if __name__ == "__main__":
    cleanup_temp_file()
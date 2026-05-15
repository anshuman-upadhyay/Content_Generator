import json


def save_metadata(folder, metadata):
    """
    Save run metadata
    """

    output_file = (
        folder["run_folder"] /
        "metadata.json"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            metadata,
            f,
            indent=4
        )

    print(
        f"Metadata saved at "
        f"{output_file}"
    )
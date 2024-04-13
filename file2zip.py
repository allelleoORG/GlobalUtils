import os
import zipfile


def file2zip(zip_filename: str, files_to_zip: list[str]) -> None:
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        for file_path in files_to_zip:
            zipf.write(file_path, os.path.basename(file_path))

# src/pytazipeach/main.py

import argparse
from pathlib import Path
import zipfile

def zip_folder(folder: Path, output_zip: Path):
    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in folder.rglob("*"):
            arcname = file.relative_to(folder)
            zf.write(file, arcname)

def main():
    parser = argparse.ArgumentParser(description="Zip each specified folder individually")
    parser.add_argument(
        "--dirs",
        nargs="+",
        required=True,
        help="List of directories to zip"
    )

    args = parser.parse_args()

    for d in args.dirs:
        folder = Path(d)

        if not folder.exists():
            print(f"Directory not found: {folder}")
            continue

        if not folder.is_dir():
            print(f"Not a directory: {folder}")
            continue

        zip_path = folder.parent / f"{folder.name}.zip"
        print(f"Zipping {folder} → {zip_path}")

        zip_folder(folder, zip_path)

    print("Done.")

# src/pytaunzip/main.py

import argparse
from pathlib import Path
import zipfile

def unzip_file(zip_path: Path):
    if not zip_path.exists():
        print(f"ZIP file not found: {zip_path}")
        return

    if not zip_path.is_file():
        print(f"Not a file: {zip_path}")
        return

    if zip_path.suffix.lower() != ".zip":
        print(f"Not a ZIP file: {zip_path}")
        return

    output_dir = zip_path.parent / zip_path.stem
    print(f"Unzipping {zip_path} → {output_dir}")

    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(output_dir)

def main():
    parser = argparse.ArgumentParser(description="Unzip specified ZIP files")
    parser.add_argument(
        "--zips",
        nargs="+",
        required=True,
        help="List of ZIP files to unzip"
    )

    args = parser.parse_args()

    for z in args.zips:
        unzip_file(Path(z))

    print("Done.")

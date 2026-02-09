# src/pytaunzipall/main.py

import argparse
from pathlib import Path
import zipfile

def unzip_file(zip_path: Path):
    output_dir = zip_path.parent / zip_path.stem
    print(f"Unzipping {zip_path} → {output_dir}")

    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(output_dir)


def main():
    parser = argparse.ArgumentParser(description="Unzip all ZIP files in a directory")
    parser.add_argument(
        "--dir",
        required=True,
        help="Directory containing ZIP files"
    )

    args = parser.parse_args()
    target = Path(args.dir)

    if not target.exists():
        print(f"Directory not found: {target}")
        return

    if not target.is_dir():
        print(f"Not a directory: {target}")
        return

    # 指定フォルダ内の ZIP を列挙
    zip_files = [p for p in target.iterdir() if p.is_file() and p.suffix.lower() == ".zip"]

    if not zip_files:
        print("No ZIP files found.")
        return

    for zip_path in zip_files:
        unzip_file(zip_path)

    print("Done.")

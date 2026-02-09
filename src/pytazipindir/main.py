# src/pytazip/main.py

import argparse
from pathlib import Path
import zipfile

def zip_folder(folder: Path, output_zip: Path):
    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in folder.rglob("*"):
            # ZIP 内のパスはフォルダ名からの相対パスにする
            arcname = file.relative_to(folder)
            zf.write(file, arcname)


def main():
    parser = argparse.ArgumentParser(description="Zip each subfolder individually")
    parser.add_argument("--dir", required=True, help="Directory containing folders to zip")

    args = parser.parse_args()
    target = Path(args.dir)

    if not target.exists():
        print(f"Directory not found: {target}")
        return

    if not target.is_dir():
        print(f"Not a directory: {target}")
        return

    # dir1 内のフォルダを列挙
    for item in target.iterdir():
        if item.is_dir():
            zip_path = target / f"{item.name}.zip"
            print(f"Zipping {item} → {zip_path}")
            zip_folder(item, zip_path)

    print("Done.")

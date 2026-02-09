# src/pytals/main.py

import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="List directory contents")
    parser.add_argument("--dir", required=True, help="Directory to list")

    args = parser.parse_args()
    target = Path(args.dir)

    if not target.exists():
        print(f"Directory not found: {target}")
        return

    if not target.is_dir():
        print(f"Not a directory: {target}")
        return

    for item in target.iterdir():
        print(item.name)

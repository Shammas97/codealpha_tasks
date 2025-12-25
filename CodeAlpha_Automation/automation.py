
"""Automation utilities:
- Move all .jpg/.jpeg files from a source folder to a destination folder.
- Extract email addresses from a .txt file and save them to an output file.

Usage:
  python automation.py move --src /path/to/dir --dst /path/to/dest
  python automation.py extract --input emails_raw.txt --output emails_out.txt
"""

import argparse
import os
import shutil
import re

EMAIL_RE = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

def move_images(src, dst, extensions=("jpg","jpeg","png")):
    os.makedirs(dst, exist_ok=True)
    moved = 0
    for root, _, files in os.walk(src):
        for f in files:
            if f.lower().split(".")[-1] in extensions:
                src_path = os.path.join(root, f)
                dst_path = os.path.join(dst, f)

                shutil.move(src_path, dst_path)
                moved += 1
    print(f"Moved {moved} files from {src} to {dst}.")

def extract_emails(input_file, output_file):
    with open(input_file, "r", encoding="utf-8", errors="ignore") as fh:
        text = fh.read()
    emails = sorted(set(EMAIL_RE.findall(text)))
    with open(output_file, "w", encoding="utf-8") as out:
        for e in emails:
            out.write(e + "\n")
    print(f"Extracted {len(emails)} unique emails to {output_file}.")

def main():
    parser = argparse.ArgumentParser(description="Small automation toolkit")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_move = sub.add_parser("move", help="Move image files")
    p_move.add_argument("--src", required=True)
    p_move.add_argument("--dst", required=True)

    p_ext = sub.add_parser("extract", help="Extract emails from text file")
    p_ext.add_argument("--input", required=True)
    p_ext.add_argument("--output", required=True)

    args = parser.parse_args()
    if args.cmd == "move":
        move_images(args.src, args.dst)
    elif args.cmd == "extract":
        extract_emails(args.input, args.output)

if __name__ == "__main__":
    main()

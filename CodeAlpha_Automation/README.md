# Automation Utilities

A small Python toolkit for automating common file and text operations:

- **Move image files**: Move `.jpg`, `.jpeg`, `.png` files from a source folder to a destination folder.
- **Extract emails**: Extract email addresses from a `.txt` file and save them to an output file.

---

## Features

1. **Move Images**
   - Moves all image files from a specified source directory to a target directory.
   - Supports `.jpg`, `.jpeg`, and `.png` by default.
   - Automatically creates the destination directory if it doesn't exist.

2. **Extract Emails**
   - Reads a text file and extracts all unique email addresses.
   - Saves the results into a specified output file.
   - Ignores duplicate emails and sorts the output.

---

## Requirements

- Python 3.6+
- No external libraries required (uses only built-in modules: `argparse`, `os`, `shutil`, `re`).

---

## Usage


python automation.py move --src /path/to/source --dst /path/to/destination
python automation.py extract --input emails_raw.txt --output emails_out.txt
python automation.py extract --input ./emails.txt --output ./unique_emails.txt


```bash
python automation.py move --src /path/to/source --dst /path/to/destination

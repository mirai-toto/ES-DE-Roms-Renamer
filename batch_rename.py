import os
import sys
from helpers import color_text
from rename_main import rename_main

ALLOWED_EXTENSIONS = {'.iso', '.nsp', '.zip', '.wua', '.chd', '.7z'}
CONFIG_PATH="rules.json"
def batch_rename(system, perform_rename, config_path):
    system_folder = os.path.expanduser(f"~/Emulation/roms/{system}")

    for filename in os.listdir(system_folder):
        file_path = os.path.join(system_folder, filename)
        if os.path.isfile(file_path) and os.path.splitext(filename)[1] in ALLOWED_EXTENSIONS:
            print(f"Processing file: {color_text(filename, '31')}")
            rename_main(filename, system, perform_rename, config_path)

if __name__ == "__main__":
    if len(sys.argv) not in [3, 4]:  # Allow 3 or 4 arguments
        print("Usage: python batch_rename.py <system> <perform_rename> [<config_path>]")
        sys.exit(1)

    system = sys.argv[1]
    perform_rename = sys.argv[2].lower() in ['true', '1', 'yes']
    config_path = sys.argv[3] if len(sys.argv) == 4 else CONFIG_PATH  # Default to rules.json

    if perform_rename:
        print("Performing batch renaming.")
    else:
        print("Running batch in dry-run mode.")

    batch_rename(system, perform_rename, config_path)

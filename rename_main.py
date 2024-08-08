import sys
import os
from file_operations import rename_rom_file, rename_media_files
from gamelist_operations import update_gamelist
from helpers import get_correct_filename, check_paths, color_text

def rename_main(filename, system, perform_rename):
    rom_file_path = os.path.expanduser(f"~/Emulation/roms/{system}/{filename}")
    media_folder = os.path.expanduser(f"~/Emulation/tools/downloaded_media/{system}")
    gamelist_path = os.path.expanduser(f"~/ES-DE/gamelists/{system}/gamelist.xml")

    if not check_paths(rom_file_path, media_folder, gamelist_path):
        return

    invalid_filename, rom_extension = os.path.splitext(filename)
    rom_extension = rom_extension.lstrip('.')  # Remove leading dot

    correct_filename = get_correct_filename(invalid_filename)

    rename_rom_file(rom_file_path, correct_filename, rom_extension, perform_rename)
    rename_media_files(media_folder, invalid_filename, correct_filename, perform_rename)
    update_gamelist(invalid_filename, correct_filename, rom_extension, gamelist_path, perform_rename)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python rename_main.py <filename> <system> <perform_rename>")
        sys.exit(1)

    filename = sys.argv[1]
    system = sys.argv[2]
    perform_rename = sys.argv[3].lower() in ['true', '1', 'yes']


    if perform_rename:
        print(color_text("Performing renaming.", "32"))  # Green text
    else:
        print(color_text("Running in dry-run mode.", "33"))  # Yellow text

    rename_main(filename, system, perform_rename)

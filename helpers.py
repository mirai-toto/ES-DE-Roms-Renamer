import os
import rules

def get_correct_filename(invalid_filename):
    updated_filename = invalid_filename

    updated_filename = rules.rename_disc_to_part(updated_filename)
    updated_filename = rules.reorder_the_in_title(updated_filename)
    updated_filename = rules.remove_unwanted_tags(updated_filename)
    updated_filename = rules.remove_unnecessary_spaces(updated_filename)
    updated_filename = rules.remove_square_bracketed_content(updated_filename)

    return updated_filename

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def check_paths(rom_file_path, media_folder, gamelist_path):
    if not os.path.isfile(rom_file_path):
        print(f"Error: ROM file path does not exist: {rom_file_path}")
        return False
    if not os.path.isdir(media_folder):
        print(f"Error: Media folder does not exist: {media_folder}")
        return False
    if not os.path.isfile(gamelist_path):
        print(f"Error: Gamelist file does not exist: {gamelist_path}")
        return False
    return True

import os
import re
import json

def remove_unnecessary_spaces(invalid_filename):
    # Remove leading, trailing, and multiple consecutive spaces
    filename = re.sub(r'\s+', ' ', invalid_filename).strip()
    # Remove spaces before .partX
    filename = re.sub(r'\s+\.part', '.part', filename)
    return filename

def load_rules_from_config(config_path):
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config['rules']

def execute_rules(invalid_filename, rules):
    updated_filename = invalid_filename

    for rule in rules:
        updated_filename = re.sub(rule['pattern'], rule['replacement'], updated_filename).strip()

    return remove_unnecessary_spaces(updated_filename)

def get_correct_filename(invalid_filename, config_path):
    rules = load_rules_from_config(config_path)
    return execute_rules(invalid_filename, rules)

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

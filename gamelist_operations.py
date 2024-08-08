import re

def update_gamelist(filename, correct_filename, rom_extension, gamelist_path, perform_rename):
    old_path = f"./{filename}.{rom_extension}"
    new_path = f"./{correct_filename}.{rom_extension}"
    
    with open(gamelist_path, 'r') as file:
        content = file.read()
    
    new_content = re.sub(rf'(<path>{old_path}</path>)', rf'<path>{new_path}</path>', content)
    
    if perform_rename:
        with open(gamelist_path, 'w') as file:
            file.write(new_content)
        print(f"Updated gamelist paths from {old_path} to {new_path}")
    else:
        print(f"Would update gamelist paths from {old_path} to {new_path}")

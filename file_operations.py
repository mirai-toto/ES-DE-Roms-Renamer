import os

def rename_rom_file(rom_file_path, correct_filename, rom_extension, perform_rename):
    new_rom_file_path = os.path.join(os.path.dirname(rom_file_path), f"{correct_filename}.{rom_extension}")
    if perform_rename:
        os.rename(rom_file_path, new_rom_file_path)
    print(f"ROM file: {rom_file_path} -> {new_rom_file_path}")

def rename_media_files(media_folder, invalid_filename, correct_filename, perform_rename):
    for root, dirs, files in os.walk(media_folder):
        for file in files:
            media_invalid_filename, ext = os.path.splitext(file)
            if media_invalid_filename == invalid_filename:
                old_media_path = os.path.join(root, file)
                new_media_path = os.path.join(root, f"{correct_filename}{ext}")
                if perform_rename:
                    os.rename(old_media_path, new_media_path)
                print(f"Media file: {old_media_path} -> {new_media_path}")

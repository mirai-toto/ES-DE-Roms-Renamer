import os

from helpers import color_text

def rename_rom_file(rom_file_path, correct_filename, rom_extension, perform_rename):
    new_rom_file_path = os.path.join(os.path.dirname(rom_file_path), f"{correct_filename}.{rom_extension}")
    if perform_rename:
        os.rename(rom_file_path, new_rom_file_path)
    relative_old_path = os.path.join("roms", os.path.basename(rom_file_path))
    relative_new_path = os.path.join("roms", os.path.basename(new_rom_file_path))
    print(f"ROM file: {color_text(relative_old_path, '33')} -> {color_text(relative_new_path, '32')}") # Yellow -> Green color

def rename_media_files(media_folder, invalid_filename, correct_filename, perform_rename):
    for root, dirs, files in os.walk(media_folder):
        for file in files:
            media_invalid_filename, ext = os.path.splitext(file)
            if media_invalid_filename == invalid_filename:
                old_media_path = os.path.join(root, file)
                new_media_path = os.path.join(root, f"{correct_filename}{ext}")
                if perform_rename:
                    os.rename(old_media_path, new_media_path)
                relative_old_path = os.path.relpath(old_media_path, media_folder)
                relative_new_path = os.path.relpath(new_media_path, media_folder)
                print(f"Media file: {color_text(relative_old_path, '33')} -> {color_text(relative_new_path, '32')}") # Yellow -> Green color
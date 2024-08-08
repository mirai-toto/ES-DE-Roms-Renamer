# ES-DE-Roms-Renamer

A Python project for renaming ROM files and associated media files, and updating gamelist XML files for emulation setups. This project helps ensure consistency and organization in your ES-DE Frontend emulation directories.

> This project has been tested on the following systems: GameCube, Nintendo DS, Nintendo Switch, PlayStation, PlayStation 2, PlayStation Portable, Wii U, Wii, GameBoy, and GameBoy Advance.

## Features
- **Rename ROM Files**: Automatically rename ROM files to cleaner versions based on predefined rules.
- **Rename Media Files**: Rename associated media files (covers, screenshots, etc.) to match the corrected ROM filenames.
- **Update Gamelist**: Modify paths in `gamelist.xml` to reflect the renamed ROM files.
- **Batch Processing**: Process all ROM files in a specified system folder.
- **File Types**: Supports `iso`, `nsp`, `zip`, `wua`, `.7z` and `chd` files.

## Requirements

- **Python 3.x**

## Installation

1. Clone the repository:

   ``` sh
   git clone https://github.com/yourusername/ES-DE-Roms-Renamer.git
   cd ES-DE-Roms-Renamer
   ```

2. Ensure you have the necessary dependencies (if any). For example, if you have a `requirements.txt` file:

   `pip install -r requirements.txt`

## Usage

### Renaming a Single ROM File

To rename a single ROM file:

   `python rename_main.py <filename> <system> <perform_rename>`

- `<filename>`: The name of the ROM file to rename (including the extension).
- `<system>`: The system folder (e.g., `gc`).
- `<perform_rename>`: Set to `true` to perform the renaming, or `false` for a dry run.

### Batch Renaming

To batch rename all ROM files in a system folder:

   `python batch_rename.py <system> <perform_rename>`

- `<system>`: The system folder (e.g., `gc`).
- `<perform_rename>`: Set to `true` to perform the renaming, or `false` for a dry run.

### Example :

   #### Renaming a single file in dry-run mode
   `python rename_main.py "Legend of Zelda.iso" "gc" "false"`

   #### Batch renaming all files in the 'gc' system folder and performing the renaming
   `python batch_rename.py "gc" "true"`


## Acknowledgments

Special thanks to the [ES-DE Frontend team](https://gitlab.com/es-de/emulationstation-de) for their great work on the ES-DE Frontend project, which inspired this tool.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

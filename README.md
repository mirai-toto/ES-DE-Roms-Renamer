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

   `python rename_main.py <filename> <system> <perform_rename> [<config_path>]`

- `<filename>`: The name of the ROM file to rename (including the extension).
- `<system>`: The system folder (e.g., `gc`).
- `<perform_rename>`: Set to `true` to perform the renaming, or `false` for a dry run.
- `[<config_path>]`: Optional. The path to the configuration file. Defaults to `rules.json` if not provided.

### Batch Renaming

To batch rename all ROM files in a system folder:

   `python batch_rename.py <system> <perform_rename> [<config_path>]`

- `<system>`: The system folder (e.g., `gc`).
- `<perform_rename>`: Set to `true` to perform the renaming, or `false` for a dry run.
- `[<config_path>]`: Optional. The path to the configuration file. Defaults to `rules.json` if not provided.

### Example

#### Renaming a single file in dry-run mode

   `python rename_main.py "Legend of Zelda.iso" "gc" "false"`

#### Renaming a single file with a custom config file

   `python rename_main.py "Legend of Zelda.iso" "gc" "true" "custom_rules.json"`

#### Batch renaming all files in the 'gc' system folder and performing the renaming

   `python batch_rename.py "gc" "true"`

#### Batch renaming all files with a custom config file

   `python batch_rename.py "gc" "true" "custom_rules.json"`

## Rule Descriptions

The following rules are used to rename ROMs, and are taken by default from the configuration file (`rules.json`).

| Pattern                             | Replacement       | Description                                                   |
|-------------------------------------|-------------------|---------------------------------------------------------------|
| `\(U\)`                             | `""`              | Remove the region code (U) indicating the USA.                |
| `\(Europe\)`                        | `""`              | Remove the region code (Europe).                              |
| `\(M\d+\)`                          | `""`              | Remove the Mx region code where x is a number.                |
| `\(Proto\)`                         | `""`              | Remove the (Proto) tag.                                       |
| `\(\d{4}-\d{2}-\d{2}\)`             | `""`              | Remove date tags like (1993-10-04).                           |
| `\(USA\)`                           | `""`              | Remove the region code (USA).                                 |
| `\(World\)`                         | `""`              | Remove the region code (World).                               |
| `\(NDSi Enhanced\)`                 | `""`              | Remove the tag (NDSi Enhanced).                               |
| `\(PSP\)`                           | `""`              | Remove the tag (PSP).                                         |
| `\(PSN\)`                           | `""`              | Remove the tag (PSN).                                         |
| `\(CGB\+SGB Enhanced\)`             | `""`              | Remove the tag (CGB+SGB Enhanced).                            |
| `\(Demo\)`                          | `""`              | Remove the tag (Demo).                                        |
| `\(DSi Enhanced\)`                  | `""`              | Remove the tag (DSi Enhanced).                                |
| `\(E\)`                             | `""`              | Remove the region code (E).                                   |
| `\(En,Fr,De\)`                      | `""`              | Remove the language code (En,Fr,De).                          |
| `\(En,Fr,De,Es\)`                   | `""`              | Remove the language code (En,Fr,De,Es).                       |
| `\(En,Fr,De,Es,It,Nl,Pt,Sv\)`       | `""`              | Remove the language code (En,Fr,De,Es,It,Nl,Pt,Sv).           |
| `\(En,Fr,De,Es,It,Nl,Sv\)`          | `""`              | Remove the language code (En,Fr,De,Es,It,Nl,Sv).              |
| `\(En,Fr,De,It\)`                   | `""`              | Remove the language code (En,Fr,De,It).                       |
| `\(En,Fr,Es\)`                      | `""`              | Remove the language code (En,Fr,Es).                          |
| `\(EU\)`                            | `""`              | Remove the region code (EU).                                  |
| `\(FR\)`                            | `""`              | Remove the region code (FR) indicating France.                |
| `\(France\)`                        | `""`              | Remove the region code (France).                              |
| `\(Japan\)`                         | `""`              | Remove the region code (Japan).                               |
| `\(Japan, USA\)`                    | `""`              | Remove the region code (Japan, USA).                          |
| `\(Kiosk\)`                         | `""`              | Remove the tag (Kiosk).                                       |
| `\(Mindscape\)`                     | `""`              | Remove the tag (Mindscape).                                   |
| `\(NTSC\)`                          | `""`              | Remove the tag (NTSC).                                        |
| `\(Promo\)`                         | `""`              | Remove the tag (Promo).                                       |
| `\(Rev \d+\)`                       | `""`              | Remove the revision tag (Rev x) where x is a number.          |
| `\(SGB Enhanced\)`                  | `""`              | Remove the tag (SGB Enhanced).                                |
| `\(UE\)`                            | `""`              | Remove the region code (UE).                                  |
| `\(Unl\)`                           | `""`              | Remove the tag (Unl) indicating an unlicensed game.           |
| `\(USA, Asia\)`                     | `""`              | Remove the region code (USA, Asia).                           |
| `\(USA, Europe\)`                   | `""`              | Remove the region code (USA, Europe).                         |
| `^(.*?), The`                       | `The $1`          | Reorder titles from 'Title, The' to 'The Title'.              |
| `\(v\d+(.\d+)*\)`                   | `""`              | Remove version tags like (v1.2.3).                            |
| `\[.*?\]`                           | `""`              | Remove content enclosed in square brackets.                   |
| `^(.*)\(Disc (\d+)\)$`              | `$1.part$2`       | Rename files ending with '(Disc x)' to '.partx'.              |
| `\s+`                               | `" "`             | Remove unnecessary spaces within the filename.                |

## Acknowledgments

Special thanks to the [ES-DE Frontend team](https://gitlab.com/es-de/emulationstation-de) for their great work on the ES-DE Frontend project, which inspired this tool.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

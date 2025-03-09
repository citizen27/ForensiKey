# ForensiKey

README made with ChatGPT.

This script extracts readable ASCII strings from a memory dump file and saves the results in both text and compressed formats.

## Features
- Reads and extracts printable ASCII strings from a memory dump file.
- Filters out short strings (default minimum length: 4 characters).
- Saves extracted keywords to a text file.
- Compresses the output into a `.zip` file for easy storage and sharing.
- Saves the output to script location.
## Requirements
- Python 3.x
- No external dependencies required

## Usage

1. Clone or download the script.
2. Run the script using Python:
 ```sh
 python script.py
 ```
3. Enter the path to the memory dump file when prompted.
4. The script will extract strings and save them to `keywords.txt`.
5. The results will also be saved in a compressed `keywords.zip` file.

## Functions Overview

### `extract_strings(file_path, min_length=4)`
Extracts readable ASCII strings from a binary file, filtering out short strings.

### `save_to_txt(keywords, filename="keywords.txt")`
Saves extracted keywords to a text file for easy reference.

### `save_to_zip(input_file="keywords.txt", zip_filename="keywords.zip")`
Compresses the output text file into a `.zip` archive.

## Example Output
After running the script, you will get:
- **`keywords.txt`** – A plain text file containing the extracted strings.
- **`keywords.zip`** – A compressed archive containing `keywords.txt`.

## License
This project is open-source and available under the MIT License.



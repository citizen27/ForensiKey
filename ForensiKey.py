import os
import zipfile
import tarfile

def extract_strings(file_path, min_length=4):
    """
    Extracts printable ASCII strings from a memory dump file.
    Strings must be at least 'min_length' characters long.
    """
    strings = []
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
            print(f"Read {len(data)} bytes from {file_path}.")
    except Exception as e:
        print(f"Error reading the file: {e}")
        return []
    
    # Look for printable ASCII characters (from space (32) to ~ (126))
    current_string = []
    for byte in data:
        if 32 <= byte <= 126:  # ASCII printable range
            current_string.append(chr(byte))
        else:
            if len(current_string) >= min_length:  # Only include strings that are at least 'min_length' long
                strings.append(''.join(current_string))
            current_string = []
    
    print(f"Extracted {len(strings)} strings.")
    return strings

def save_to_txt(keywords, filename="keywords.txt"):
    """Save the extracted keywords to a text file."""
    with open(filename, 'w') as f:
        for keyword in keywords:
            f.write(f"{keyword}\n")
    print(f"Saved to {filename}")

def save_to_zip(input_file="keywords.txt", zip_filename="keywords.zip"):
    """Save a file to a zip archive."""
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(input_file)
    print(f"Saved to {zip_filename}")

def main():
    # Ask the user for the memory dump file path
    dump_file = input("Path to memory file: ")

    if not os.path.exists(dump_file):
        print(f"Error: The file {dump_file} does not exist.")
        return
    
    # 1. Extract printable strings from the memory dump
    print("Extracting strings from the memory dump...")
    extracted_strings = extract_strings(dump_file)
    if not extracted_strings:
        print("No strings were extracted from the memory dump.")
        return
        
    keywords = [keyword for keyword in extracted_strings if len(keyword) > 3]  # Example filter
    print(f"Filtered down to {len(keywords)} keywords.")
    
    # 2. Save the results
    save_to_txt(keywords)

    # 3. Save to compressed formats (.zip, .tar.gz)
    save_to_zip("keywords.txt")

if __name__ == "__main__":
    main()

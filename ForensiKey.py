import os
import csv
import zipfile
import tarfile
from collections import Counter

def extract_strings(file_path, min_length=4):
    """
    Extracts printable ASCII strings from a memory dump file.
    Strings must be at least 'min_length' characters long.
    """
    strings = []
    with open(file_path, 'rb') as f:
        data = f.read()

    # Look for printable ASCII characters (from space (32) to ~ (126))
    current_string = []
    for byte in data:
        if 32 <= byte <= 126:  # ASCII printable range
            current_string.append(chr(byte))
        else:
            if len(current_string) >= min_length:  # Only include strings that are at least 'min_length' long
                strings.append(''.join(current_string))
            current_string = []
    
    return strings

def calculate_frequencies(keywords):
    """
    Calculate the frequency of each keyword in the list.
    Returns a dictionary of keyword frequencies.
    """
    return dict(Counter(keywords))

def save_to_txt(keyword_freq, filename="keywords.txt"):
    """Save keyword frequency data to a text file."""
    with open(filename, 'w') as f:
        for keyword, freq in keyword_freq.items():
            f.write(f"{keyword}\n")
    print(f"Saved to {filename}")

def save_to_csv(keyword_freq, filename="keywords.csv"):
    """Save keyword frequency data to a CSV file."""
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Keyword", "Frequency"])  # Column headers
        for keyword, freq in keyword_freq.items():
            writer.writerow([keyword, freq])
    print(f"Saved to {filename}")

def save_to_zip(input_file="keywords.txt", zip_filename="keywords.zip"):
    """Save a file to a zip archive."""
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(input_file)
    print(f"Saved to {zip_filename}")

def save_to_tar(input_file="keywords.txt", tar_filename="keywords.tar.gz"):
    """Save a file to a tar.gz archive."""
    with tarfile.open(tar_filename, "w:gz") as tar:
        tar.add(input_file)
    print(f"Saved to {tar_filename}")

def main():
    # 1. Specify the memory dump file
    dump_file = input("Path to memory file:")  # Change this to the path of your memory dump file
    
    # 2. Extract printable strings from the memory dump
    extracted_strings = extract_strings(dump_file)
    print(f"Extracted {len(extracted_strings)} strings from the dump.")
    
    # 3. Filter the extracted strings (you can customize this part)
    keywords = [keyword for keyword in extracted_strings if len(keyword) > 3]  # Example filter

    # 4. Calculate the frequency of each keyword
    keyword_freq = calculate_frequencies(keywords)
    print(f"Found {len(keyword_freq)} unique keywords.")

    # 5. Choose the output format and save results
    # Save as .txt file
    save_to_txt(keyword_freq)

    # Save as .csv file
    save_to_csv(keyword_freq)

    # Optionally, save to compressed formats (.zip, .tar.gz)
    save_to_zip("keywords.txt")
    save_to_tar("keywords.txt")

if __name__ == "__main__":
    main()

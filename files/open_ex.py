#!/usr/bin/env python3


def read(file_path: str) -> str:
    try:
        # Modes:
        # 'r'  - Read (default). Opens for reading. Error if file doesn't exist.
        # 'rb' - Read Binary. Used for non-text files (images, PDFs).
        # 'r+' - Read and Write.
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            print("File content successfully loaded.")
            return content
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except PermissionError:
        print(f"Error: You don't have permissions to read {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def write(file_path: str, text_to_write: str) -> None:
    try:
        # Modes:
        # 'w'  - Write. Creates a new file or truncates (overwrites) existing.
        # 'wb' - Write Binary.
        # 'a'  - Append. Adds content to the end of the file without overwriting.
        # 'w+' - Write and Read.
        # 'x'  - Exclusive creation. Fails if the file already exists.
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_to_write)
            print(f"Successfully written to {file_path}")
    except OSError as e:
        # Catching input/output errors (disk full, etc.)
        print(f"Error: Could not write to file. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    write("output.txt", "Hello, world!")
    data = read("output.txt")
    print(data)

#!/usr/bin/env python3

"""
The advantages of using pathlib over open() include better handling of file paths and enhanced readability.
pathlib provides an object-oriented interface, making it easier to handle file paths and perform file operations reliably and clearly.
"""

from pathlib import Path


def read(file: str) -> str | None:
    try:
        file_path = Path(file)
        return file_path.read_text()
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except PermissionError:
        print(f"Error: You don't have permissions to read {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def write(file: str, content: str) -> None:
    try:
        file_path = Path(file)
        file_path.write_text(content)
    except OSError as e:
        # Catching input/output errors (disk full, etc.)
        print(f"Error: Could not write to file. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    write("output.txt", "Hello, world!")
    data = read("output.txt")
    print(data)

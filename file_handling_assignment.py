# File Handling Assignment Script

def create_file():
    try:
        # Create and write to a new file in write mode
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is line 1.\n")
            file.write("The number 42 is present here.\n")
            file.write("Python file handling is cool.\n")
        print("File created and written successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File creation process is done.\n")


def read_file():
    try:
        # Read the file content
        with open("my_file.txt", 'r') as file:
            content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    finally:
        print("File reading process is done.\n")


def append_file():
    try:
        # Append to the file in append mode
        with open("my_file.txt", 'a') as file:
            file.write("Here is an additional line.\n")
            file.write("The number 99 has been appended.\n")
            file.write("Appending is complete.\n")
        print("Text appended successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File appending process is done.\n")


# Main function to demonstrate the process
def main():
    create_file()    # Step 1: Create and write to the file
    read_file()      # Step 2: Read the file content
    append_file()    # Step 3: Append more text to the file
    read_file()      # Step 4: Read the file again to confirm appending


if __name__ == "__main__":
    main()

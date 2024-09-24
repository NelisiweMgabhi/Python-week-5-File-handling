# Python-week-5-File-handling

Script Breakdown:
create_file(): Creates a file named my_file.txt and writes three lines of text into it.
read_file(): Reads and displays the file's content.
append_file(): Opens the file in append mode and adds three more lines of text.
Error Handling: All file-related operations are enclosed in try, except, and finally blocks to manage potential exceptions such as FileNotFoundError and PermissionError.
main(): This function executes the process sequentially:
Creates the file and writes initial content.
Reads and displays the file.
Appends more content to the file.
Reads the file again to confirm the appended content.
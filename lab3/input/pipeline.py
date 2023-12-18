from pathlib import Path

FILE_SRC_PATH = Path(r"C:\Users\mwicz\Documents\Czarnowski\-Exploration-of-internet-resources\lab3\input\apache_logs.txt")
FILE_DEST_PATH = Path(r"C:\Users\mwicz\Documents\Czarnowski\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")
UNUSABLE_ROW = [
    "GET /style2.css HTTP/1.1",
    "GET /favicon.ico HTTP/1.1",
    "GET /reset.css HTTP/1.1"
]

def is_row_usable(row: str) -> bool:
    for unsuable in UNUSABLE_ROW:       
        if unsuable in row:
            return False
    return True

def clean_rows_and_save_to_new_file():
    with open(FILE_SRC_PATH, "r") as src_file, open(FILE_DEST_PATH, "w") as dest_file:
        while line := src_file.readline():
            stripped_line = line.rstrip()
            if is_row_usable(stripped_line):
                dest_file.write(f"{stripped_line}\n")


clean_rows_and_save_to_new_file()

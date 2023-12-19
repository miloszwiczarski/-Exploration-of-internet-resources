from pathlib import Path

FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")

with open(FILE_SRC_PATH, 'r') as file:
    lines = file.readlines()

total_visits = len(lines)
print(f"Całkowita liczba wizyt: {total_visits}")

import re
import os
from pathlib import Path

FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")
FILE_DEST_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\output\bot_finder.txt")

# Otwarcie pliku z logami
with open(FILE_SRC_PATH, 'r') as file:
    lines = file.readlines()

# Definicja bardziej szczegółowego wzorca dla robotów internetowych
robot_pattern = re.compile(r'(Googlebot|Baiduspider|Sogou|bingbot|YandexBot|' 
                           r'msnbot|Twitterbot|DuckDuckBot|Exabot|AhrefsBot)',
                           re.IGNORECASE)

# Lista przechowująca wpisy dotyczące robotów internetowych
robot_entries = []

# Iteracja przez każdą linię w pliku logów
for line in lines:
    if re.search(robot_pattern, line):
        # Jeśli linia pasuje do wzorca robota internetowego, dodaj ją do listy
        robot_entries.append(line)

# Otwarcie pliku do zapisu wyników w folderze output
with open(FILE_DEST_PATH, 'w') as output_file:
    # Zapisanie znalezionych wpisów dotyczących robotów internetowych
    if len(robot_entries) > 0:
        output_file.write("Found entries regarding internet robots:\n")
        for entry in robot_entries:
            output_file.write(entry)
        output_file.write("\n")
    else:
        output_file.write("There are no entries for web crawlers in the dataset.")

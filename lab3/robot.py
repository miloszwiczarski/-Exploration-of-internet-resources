import re

# Otwarcie pliku z logami
with open('cleaned_apache_logs.txt', 'r') as file:
    lines = file.readlines()

# Definicja wzorca dla robotów internetowych
robot_pattern = re.compile(r'bot|crawl|spider', re.IGNORECASE)

# Lista przechowująca wpisy dotyczące robotów internetowych
robot_entries = []

# Iteracja przez każdą linię w pliku logów
for line in lines:
    if re.search(robot_pattern, line):
        # Jeśli linia pasuje do wzorca robota internetowego, dodaj ją do listy
        robot_entries.append(line)

# Nazwa pliku do zapisu wyników
output_file_name = 'znalezione_roboty.txt'

# Otwarcie pliku do zapisu wyników
with open(output_file_name, 'w') as output_file:
    # Zapisanie znalezionych wpisów dotyczących robotów internetowych
    if len(robot_entries) > 0:
        output_file.write("Znalezione wpisy dotyczące robotów internetowych:\n")
        for entry in robot_entries:
            output_file.write(entry)
        output_file.write("\n")
    else:
        output_file.write("Brak wpisów dotyczących robotów internetowych w zbiorze danych.")

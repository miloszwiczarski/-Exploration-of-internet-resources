from collections import defaultdict
from pathlib import Path

FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")
FILE_DEST_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\output\highest_request_resources.txt")

# Odczyt danych z pliku
with open(FILE_SRC_PATH, 'r') as file:
    data = file.readlines()

# Tworzenie słownika dla przechowywania liczby żądań dla każdego zasobu
resource_count = defaultdict(int)

# Iteracja przez każdą linię danych i zliczanie żądań dla zasobów
for line in data:
    resource = line.split()[6]
    resource_count[resource] += 1

# Sortowanie zasobów według liczby żądań
sorted_resources = sorted(resource_count.items(), key=lambda x: x[1], reverse=True)

# Zapis wyników do pliku
with open(FILE_DEST_PATH, 'w') as output_file:
    output_file.write("Top requested resources:\n")
    for resource, count in sorted_resources[:10]:
        output_file.write(f"{resource}: {count} requests\n")


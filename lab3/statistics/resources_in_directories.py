from collections import Counter
from pathlib import Path

FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")
FILE_DEST_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\output\resources_in_directories.txt")

# 15 zad

def read_log_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

def analyze_logs(log_data):
    directories_resources = {}

    # Zliczenie żądań dla zasobów w poszczególnych katalogach
    for line in log_data:
        splits = line.split('"')
        resource = splits[1].split()[1]
        directory = resource.split('/', 2)[1] if len(resource.split('/')) > 2 else resource

        if directory not in directories_resources:
            directories_resources[directory] = Counter()

        directories_resources[directory][resource] += 1

    # Katalogi i zasoby o największej liczbie żądań
    most_requested_directories_resources = {
        directory: resources.most_common(5) for directory, resources in directories_resources.items()
    }

    return most_requested_directories_resources

# Odczytanie danych z pliku
log_data = read_log_file(FILE_SRC_PATH)

# Analiza danych
most_requested_directories_resources = analyze_logs(log_data)

# Zapis wyników do pliku
with open(FILE_DEST_PATH, 'w') as result_file:
    result_file.write("Most requested resources in directories:\n")
    for directory, resources in most_requested_directories_resources.items():
        result_file.write(f"{directory}:\n")
        for resource, count in resources:
            result_file.write(f"\t{resource}: {count} requests\n")

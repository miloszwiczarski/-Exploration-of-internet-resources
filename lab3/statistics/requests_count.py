from collections import Counter
from pathlib import Path

FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")
FILE_DEST_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\output\requests_count.txt")


def read_log_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()


def analyze_logs(log_data):
    resources = []
    directories = []

    # Odczytanie zasobów i katalogów
    for line in log_data:
        splits = line.split('"')
        resource = splits[1].split()[1]
        directory = resource.split('/', 2)[1] if len(resource.split('/')) > 2 else resource

        resources.append(resource)
        directories.append(directory)

    # Zliczenie żądań dla zasobów i katalogów
    resource_counter = Counter(resources)
    directory_counter = Counter(directories)

    # Zasoby o największej liczbie żądań
    most_requested_resources = resource_counter.most_common(5)

    # Katalogi o największej liczbie żądań
    most_requested_directories = directory_counter.most_common(5)

    return most_requested_resources, most_requested_directories


# Odczytanie danych z pliku
log_data = read_log_file(FILE_SRC_PATH)

# Analiza danych
most_requested_resources, most_requested_directories = analyze_logs(log_data)

# Zapis wyników do pliku
with open(FILE_DEST_PATH, 'w') as result_file:
    result_file.write("Most requested resources:\n")
    for resource, count in most_requested_resources:
        result_file.write(f"{resource}: {count} requests\n")

    result_file.write("\nMost frequently requested directories:\n")
    for directory, count in most_requested_directories:
        result_file.write(f"{directory}: {count} requests\n")






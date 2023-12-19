import re
from pathlib import Path
from datetime import datetime

FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")


with open(FILE_SRC_PATH, 'r') as file:
    logs = file.readlines()

# Wyrażenie regularne do ekstrakcji czasów
time_pattern = r'\[(.*?)\]'
times = []

# Wyszukiwanie czasów w logach
for line in logs:
    match = re.search(time_pattern, line)
    if match:
        time_str = match.group(1)
        # Konwersja na obiekt datetime
        time_obj = datetime.strptime(time_str, '%d/%b/%Y:%H:%M:%S %z')
        times.append(time_obj)

# Sortowanie czasów
times.sort()

# Obliczanie różnic czasowych
time_diffs = [(times[i + 1] - times[i]).total_seconds() for i in range(len(times) - 1)]

# Znalezienie minimalnego czasu
min_time = min(time_diffs)

# Wyświetlenie minimalnego czasu wizyty
print(f"Najkrótszy czas wizyty: {min_time} sekund")

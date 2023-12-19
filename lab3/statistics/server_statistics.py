from datetime import datetime
from collections import defaultdict
from datetime import datetime
from pathlib import Path

FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")


with open(FILE_SRC_PATH, 'r') as file:
    logs = file.readlines()

# Tworzymy słownik, aby przechowywać liczbę żądań dla każdego unikalnego dnia
requests_per_day = defaultdict(int)

# Przetwarzamy każdą linię logu
for log in logs:
    parts = log.split('[')  # Dzielimy log według nawiasów kwadratowych '['
    if len(parts) > 1:
        date_str = parts[1].split()[0]  # Pobieramy datę z logu
        date = datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S')  # Konwertujemy na obiekt daty
        day = date.strftime('%Y-%m-%d')  # Formatujemy datę do postaci 'RRRR-MM-DD'
        requests_per_day[day] += 1  # Zwiększamy liczbę żądań dla danego dnia

# Wyświetlamy statystyki wykorzystania serwera w poszczególnych dniach
for day, count in requests_per_day.items():
    print(f"{day}: {count} requests")

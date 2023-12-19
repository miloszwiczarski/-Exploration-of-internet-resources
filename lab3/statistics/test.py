from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt  
from pathlib import Path


FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")


# Odczytanie pliku z logami
with open(FILE_SRC_PATH, 'r') as file:
    logs = file.readlines()

# Słowniki do przechowywania statystyk
hours_count = defaultdict(int)
weekdays_count = defaultdict(int)
dayparts_count = defaultdict(int)

# Iteracja przez każdą linię logu
for log in logs:
    log_parts = log.split('[')[1].split(']')[0].split()
    timestamp = datetime.strptime(log_parts[0], '%d/%b/%Y:%H:%M:%S')
    
    # Statystyki dla godzin
    hour = timestamp.hour
    hours_count[hour] += 1
    
    # Statystyki dla dni tygodnia (0 - poniedziałek, 6 - niedziela)
    weekday = timestamp.weekday()
    weekdays_count[weekday] += 1
    
    # Statystyki dla por part of the day
    if 6 <= hour < 12:
        dayparts_count['morning'] += 1
    elif 12 <= hour < 18:
        dayparts_count['afternoon'] += 1
    elif 18 <= hour < 24:
        dayparts_count['evening'] += 1
    else:
        dayparts_count['night'] += 1

# Wyświetlenie wyników
print("Statystyka wykorzystania serwera w poszczególnych godzinach:")
for hour, count in sorted(hours_count.items()):
    print(f"Godzina {hour}:00 - {hour + 1}:00 -> {count} żądań")

print("\nStatystyka wykorzystania serwera w poszczególnych dniach tygodnia:")
days = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
for weekday, count in sorted(weekdays_count.items()):
    print(f"{days[weekday]} -> {count} żądań")

print("\nStatystyka wykorzystania serwera w porach dnia:")
for part, count in sorted(dayparts_count.items()):
    print(f"{part.capitalize()} -> {count} żądań")

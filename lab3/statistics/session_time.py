from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import statistics
from pathlib import Path
from statistics import mean

FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")

# Słownik do przechowywania czasów sesji dla każdego adresu IP
session_times = defaultdict(list)

# Otwarcie pliku i analiza logów
with open(FILE_SRC_PATH, 'r') as file:
    for line in file:
        elements = line.split(' ')
        ip_address = elements[0]
        timestamp = elements[3][1:] + ' ' + elements[4][:-1]  # Pobranie daty i godziny

        # Parsowanie daty
        log_time = datetime.strptime(timestamp, '%d/%b/%Y:%H:%M:%S %z')

        # Dodanie czasu sesji do listy dla danego adresu IP
        session_times[ip_address].append(log_time)

# Obliczenie czasu trwania sesji dla każdego adresu IP w minutach
session_durations = {}
for ip, times in session_times.items():
    if len(times) >= 2:
        times.sort()
        duration = (max(times) - min(times)).total_seconds() / 60.0  # Czas trwania w minutach
        session_durations[ip] = duration

# Wypisanie typowego czasu trwania sesji dla danego adresu IP
for ip, duration in session_durations.items():
    print(f"Typowy czas dla IP {ip}: {duration:.2f} minut")


# Obliczenie średniego czasu trwania sesji
average_duration = mean(session_durations.values())
print(f"Średni czas trwania sesji: {average_duration:.2f} minut")


# Zbudowanie histogramu czasów sesji w minutach
plt.hist(list(session_durations.values()), bins=30, edgecolor='black')
plt.xlabel('Czas sesji (w minutach)')
plt.ylabel('Liczba sesji')
plt.title('Histogram czasów sesji')
plt.text(average_duration, plt.ylim()[1]*0.9, f'Średni czas trwania sesji: {average_duration:.2f} minut', fontsize=10)

plt.show()

from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")
FILE_DEST_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\output\requests_sesions_correlation.png")

# Słownik do przechowywania czasów sesji dla każdego adresu IP
session_times = defaultdict(list)
requests_count = defaultdict(int)

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
        
        # Zliczanie liczby żądań dla danego adresu IP
        requests_count[ip_address] += 1

# Obliczenie długości sesji dla każdego adresu IP
session_lengths = {}
for ip, times in session_times.items():
    if len(times) >= 2:
        times.sort()
        duration = (max(times) - min(times)).total_seconds() / 60.0  # Czas trwania w minutach
        session_lengths[ip] = duration

# Zbieranie liczby żądań dla każdej sesji
requests_per_session = [requests_count[ip] for ip in session_lengths if ip in requests_count]

# Wykres zależności między długością sesji a liczbą żądań
plt.scatter(list(session_lengths.values()), requests_per_session, alpha=0.5)
plt.xlabel('Długość sesji (w minutach)')
plt.ylabel('Liczba żądań')
plt.title('Zależność między długością sesji a liczbą żądań')
plt.savefig(FILE_DEST_PATH)
plt.show()

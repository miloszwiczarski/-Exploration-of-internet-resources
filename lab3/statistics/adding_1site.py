from datetime import datetime
from collections import defaultdict
import statistics
from pathlib import Path

FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")

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
        duration = (max(times) - min(times)).total_seconds() # Czas trwania w minutach
        session_lengths[ip] = duration

# Średnia długość sesji
average_session_length = statistics.mean(session_lengths.values())

# Średnia liczba żądań stron na sesję
average_requests_per_session = statistics.mean(requests_count.values())

# Różnica w długości sesji z dodatkową stroną
difference_in_session_length = 1  # Załóżmy dodatkową stronę

# Obliczenie o ile średnio wydłuży się sesja po dodaniu dodatkowej strony
additional_page_extension = difference_in_session_length * average_requests_per_session

# Obliczenie, o ile średnio wydłuży się sesja
average_session_extension = additional_page_extension / average_session_length

print(average_session_extension)

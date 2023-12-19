from collections import defaultdict
import matplotlib.pyplot as plt
from pathlib import Path

FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")
FILE_DEST_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\output\histogram_of_a_distribution.png")

# Wczytanie danych z pliku
with open(FILE_SRC_PATH, 'r') as file:
    logs = file.readlines()

# Tworzenie słownika do przechowywania liczby żądań dla każdej sesji
session_requests = defaultdict(int)

# Przetwarzanie danych i zliczanie liczby żądań w sesji
for log in logs:
    parts = log.split()
    if len(parts) > 3:
        ip_address, timestamp, request = parts[0], parts[3], parts[6]
        session_requests[ip_address] += 1

# Zbudowanie histogramu
requests_count = list(session_requests.values())
plt.hist(requests_count, bins=range(1, 21), align='left')  # Zakres od 1 do 20 z krokiem co 1
plt.xlabel('Liczba żądań w sesji')
plt.ylabel('Liczba sesji')
plt.title('Histogram liczby żądań w sesji')
plt.savefig(FILE_DEST_PATH)
plt.show()

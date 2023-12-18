from collections import Counter
from urllib.parse import urlparse
import os
from pathlib import Path

FILE_SRC_PATH = Path(r"C:\Users\mwicz\Documents\Czarnowski\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")
FILE_DEST_PATH = Path(r"C:\Users\mwicz\Documents\Czarnowski\-Exploration-of-internet-resources\lab3\output\statistics.txt")



# Odczytanie danych z pliku
with open(FILE_SRC_PATH, 'r') as file:
    logs = file.readlines()

# Zadanie 10: Ile różnych żądań zostało zarejestrowanych w analizowanym pliku logs?
unique_requests = set()
for log in logs:
    request = log.split('"')[1].split()[1]
    unique_requests.add(request)
num_unique_requests = len(unique_requests)

# Zapis wyniku do pliku
with open(FILE_DEST_PATH, 'w') as output_file:
    output_file.write(f"Number of different requests: {num_unique_requests}\n\n")

# Zadanie 11: Skąd były najczęstsze żądania?
ip_counter = Counter()
for log in logs:
    ip_address = log.split()[0]
    ip_counter[ip_address] += 1

most_common_ips = ip_counter.most_common(5)  # Pobierz 5 najczęściej występujących adresów IP

# Zapis wyniku do pliku
with open(FILE_DEST_PATH, 'a') as output_file:
    output_file.write("Most common IP addresses:\n")
    for ip, count in most_common_ips:
        output_file.write(f"{ip}: {count} requests\n")
    output_file.write("\n")

# Zadanie 12: Zidentyfikowanie najczęściej odwiedzanych stron podczas zidentyfikowanych sesji
session_pages = {}
for log in logs:
    ip, timestamp, request = log.split(maxsplit=2)
    if ip not in session_pages:
        session_pages[ip] = []
    session_pages[ip].append(request)

# Wyznaczenie najczęściej odwiedzanych stron w sesjach
page_counter = Counter()
for ip, pages in session_pages.items():
    page_counter.update(pages)

most_common_pages = page_counter.most_common(5)  # Pobierz 5 najczęściej odwiedzanych stron

# Zapis wyniku do pliku
with open(FILE_DEST_PATH, 'a') as output_file:
    output_file.write("Most visited pages:\n")
    for page, count in most_common_pages:
        output_file.write(f"{page}: {count} visits\n")
    output_file.write("\n")


# Zadanie 13: Czy te najczęściej odwiedzane strony były odwiedzane jako jedne z pierwszych w sesji?
most_common_pages_first_in_session = set()
for ip, pages in session_pages.items():
    if len(pages) > 0:
        most_common_page = page_counter.most_common(1)[0][0]
        if most_common_page in pages:
            most_common_pages_first_in_session.add(most_common_page)

# Zapis wyniku do pliku
with open(FILE_DEST_PATH, 'a') as output_file:
    output_file.write("The most frequently visited pages are among the first in the session:\n")
    if len(most_common_pages_first_in_session) > 0:
        for page in most_common_pages_first_in_session:
            output_file.write(f"{page}\n")
    else:
        output_file.write("No such pages\n")
    output_file.write("\n")



from collections import Counter
from urllib.parse import urlparse

# Otwarcie pliku i odczytanie danych
with open('cleaned_apache_logs.txt', 'r') as file:
    logs = file.readlines()

# Zadanie 10: Ile różnych żądań zostało zarejestrowanych w analizowanym pliku logs?
unique_requests = set()
for log in logs:
    request = log.split('"')[1].split()[1]
    unique_requests.add(request)
num_unique_requests = len(unique_requests)

# Zapis wyniku do pliku
with open('wyniki.txt', 'w') as output_file:
    output_file.write(f"Ilość różnych żądań: {num_unique_requests}\n\n")

# Zadanie 11: Skąd były najczęstsze żądania?
ip_counter = Counter()
for log in logs:
    ip_address = log.split()[0]
    ip_counter[ip_address] += 1

most_common_ips = ip_counter.most_common(5)  # Pobierz 5 najczęściej występujących adresów IP

# Zapis wyniku do pliku
with open('wyniki.txt', 'a') as output_file:
    output_file.write("Najczęstsze adresy IP:\n")
    for ip, count in most_common_ips:
        output_file.write(f"{ip}: {count} żądań\n")
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
with open('wyniki.txt', 'a') as output_file:
    output_file.write("Najczęściej odwiedzane strony:\n")
    for page, count in most_common_pages:
        output_file.write(f"{page}: {count} odwiedzeń\n")
    output_file.write("\n")

# Zadanie 13: Czy najczęściej odwiedzane strony były odwiedzane jako pierwsze w sesji?
first_requests = {}
for log in logs:
    ip, timestamp, request = log.split(maxsplit=2)
    if ip not in first_requests:
        first_requests[ip] = request

# Zapis wyniku do pliku
with open('wyniki.txt', 'a') as output_file:
    output_file.write("Najczęściej odwiedzane strony jako pierwsze w sesji:\n")
    for ip, first_request in first_requests.items():
        if any(first_request in page for page, _ in most_common_pages):
            output_file.write(f"{ip}: {first_request}\n")

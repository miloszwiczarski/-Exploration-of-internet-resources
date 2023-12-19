from pathlib import Path

# 31. Jak jest całkowita liczba różnych użytkowników?
FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")

unique_users = set()

with open(FILE_SRC_PATH, 'r') as file:
    
    for line in file:
        ip_address = line.split(' ')[0]
        unique_users.add(ip_address)

total_unique_users = len(unique_users)
print("31: Całkowita liczba różnych użytkowników:", total_unique_users)


# 32. Jaka jest liczba użytkowników, jaka odwiedziła więcej niż jedną stronę, a ile takich którzy
# mieli więcej niż jedną sesję danego dnia?

from collections import defaultdict
from datetime import datetime
from pathlib import Path

FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")

with open(FILE_SRC_PATH, 'r') as file:
    logs = file.readlines()

# Inicjalizacja słowników dla unikalnych odwiedzin stron i sesji użytkowników
unique_page_visits = defaultdict(set)
session_count = defaultdict(set)

# Przetwarzanie logów
for log in logs:
    # Dzielenie logu na poszczególne pola
    log_parts = log.split(' ')
    ip_address = log_parts[0]
    timestamp = log_parts[3][1:]  # Pominięcie '[' z timestampu
    
    # Dodanie adresu IP do listy unikalnych odwiedzin stron
    unique_page_visits[timestamp].add(ip_address)
    
    # Dodanie adresu IP do listy sesji użytkownika
    session_count[ip_address].add(timestamp)

# Liczenie unikalnych użytkowników, którzy odwiedzili więcej niż jedną stronę
users_multiple_page_visits = sum(1 for visits in unique_page_visits.values() if len(visits) > 1)

# Liczenie użytkowników, którzy mieli więcej niż jedną sesję danego dnia
users_multiple_sessions = sum(1 for sessions in session_count.values() if len(sessions) > 1)

print(f"32: Liczba użytkowników, którzy odwiedzili więcej niż jedną stronę: {users_multiple_page_visits}")
print(f"32: Liczba użytkowników, którzy mieli więcej niż jedną sesję danego dnia: {users_multiple_sessions}")




# 33. Jaka jest średnia liczba wizyt dla użytkownika?
from collections import defaultdict

with open(FILE_SRC_PATH, 'r') as file:
    lines = file.readlines()


user_visits = defaultdict(int)


for line in lines:

    fields = line.split(' ')

    ip_address = fields[0]

    user_visits[ip_address] += 1


total_visits = sum(user_visits.values())
average_visits = total_visits / len(user_visits)

print(f"33: Średnia liczba wizyt dla użytkownika: {average_visits}")

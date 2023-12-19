from datetime import datetime
from pathlib import Path

FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")

def calculate_average_time(log_file_path):
    # Słownik do przechowywania informacji o czasie wejścia i wyjścia na stronie dla każdego użytkownika
    user_times = {}

    with open(log_file_path, 'r') as file:
        for line in file:
            data = line.split()
            ip_address = data[0]
            timestamp = data[3][1:] + ' ' + data[4][:-1]  # Pobranie znacznika czasu
            timestamp = datetime.strptime(timestamp, '%d/%b/%Y:%H:%M:%S %z')

            if ip_address not in user_times:
                user_times[ip_address] = {'entry_time': timestamp, 'total_time': 0, 'count': 0}
            else:
                # Obliczenie różnicy czasu wejścia i wyjścia
                time_spent = timestamp - user_times[ip_address]['entry_time']
                user_times[ip_address]['total_time'] += time_spent.total_seconds()
                user_times[ip_address]['entry_time'] = timestamp
                user_times[ip_address]['count'] += 1

    total_time = 0
    total_visits = 0

    # Obliczenie sumy czasów i liczby wejść na stronę
    for user in user_times:
        total_time += user_times[user]['total_time']
        total_visits += user_times[user]['count']

    # Obliczenie średniego czasu przebywania na stronie
    average_time = total_time / total_visits if total_visits > 0 else 0
    return average_time

# Przykładowe wywołanie funkcji z podaniem ścieżki do pliku z logami

average_time_spent = calculate_average_time(FILE_SRC_PATH)
print(f"Średni czas przebywania na stronie: {average_time_spent / 60} sekund")

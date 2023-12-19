from datetime import datetime 
from pathlib import Path  
import matplotlib.pyplot as plt  


FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")
FILE_DEST_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\output\more_than_one_session_time.png")
#
def calculate_average_time_per_page(log_file):
    sessions = {}
    
    with open(log_file, 'r') as file:
     
        for line in file:
            # Podział linii na elementy po spacji
            elements = line.split(' ')
            timestamp = elements[3][1:] + ' ' + elements[4][:-1]  # Wyodrębnienie znaczącego czasu
            ip_address = elements[0]  # Pobranie adresu IP

            # Jeśli adres IP nie istnieje w słowniku, dodaj go
            if ip_address not in sessions:
                sessions[ip_address] = {'last_request_time': None, 'total_time': 0, 'count': 0}

            # Konwersja znaczącego czasu na obiekt daty i czasu
            current_time = datetime.strptime(timestamp, '%d/%b/%Y:%H:%M:%S %z')

            # Obliczenie różnicy czasu między żądaniami
            if sessions[ip_address]['last_request_time'] is not None:
                time_diff = current_time - sessions[ip_address]['last_request_time']
                sessions[ip_address]['total_time'] += time_diff.total_seconds()
                sessions[ip_address]['count'] += 1

            sessions[ip_address]['last_request_time'] = current_time

    # Sesje z więcej niż jednym żądaniem
    multiple_requests_sessions = [session_data for session_data in sessions.values() if session_data['count'] > 1]

    if not multiple_requests_sessions:
        return None

    # Obliczenie średniego czasu na stronę 
    total_times = [session['total_time'] / session['count'] for session in multiple_requests_sessions]
    average_time = sum(total_times) / len(total_times)
    return total_times, average_time

# Wywołanie funkcji i pobranie wyniku
result = calculate_average_time_per_page(FILE_SRC_PATH)

if result:
    total_times, average_time = result
    # Wyświetlenie informacji o rozkładzie czasu na stronę i średnim czasie dla sesji
    print(f"Rozkład średniego czasu na stronę dla sesji składających się z więcej niż jednego żądania: {total_times}")
    print(f"Średni czas na stronę dla takich sesji: {average_time/60} sekund")
else:
    print("Brak ")

# Wykres punktowy
plt.scatter(range(len(total_times)), total_times)  
plt.xlabel('Indeks sesji') 
plt.ylabel('Średni czas (sekundy)') 
plt.title('Rozkład średniego czasu na stronę dla sesji z więcej niż jednym żądaniem') 
plt.savefig(FILE_DEST_PATH)
plt.show() 

from datetime import datetime
from collections import defaultdict
from pathlib import Path

FILE_SRC_PATH = Path(r"C:\Users\mwicz\Documents\Czarnowski\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")
FILE_DEST_PATH = Path(r"C:\Users\mwicz\Documents\Czarnowski\-Exploration-of-internet-resources\lab3\output\session_analysis.txt")

# Funkcja do analizy czasu i identyfikacji sesji użytkownika
def identify_sessions(log_file):
    # Słownik przechowujący sesje użytkowników
    sessions = defaultdict(list)

    with open(log_file, 'r') as file:
        for line in file:
            # Dla każdej linii w pliku cleaned_apache_logs.txt
            split_line = line.split()
            if len(split_line) > 3:
                ip_address = split_line[0]
                timestamp = split_line[3].lstrip('[')
                timestamp = datetime.strptime(timestamp, '%d/%b/%Y:%H:%M:%S')

                # Dodanie adresu IP i znacznika czasu do słownika sesji
                sessions[ip_address].append(timestamp)

    # Sortowanie znaczników czasu dla każdego adresu IP
    for ip, timestamps in sessions.items():
        sessions[ip] = sorted(timestamps)

    # Identyfikacja sesji użytkownika na podstawie interwałów czasowych
    session_results = {}
    for ip, timestamps in sessions.items():
        session_intervals = []
        current_session = [timestamps[0]]

        for i in range(1, len(timestamps)):
            time_diff = (timestamps[i] - timestamps[i - 1]).total_seconds()

            if time_diff <= 900:  # Założenie: Sesja trwa maksymalnie 15 minut (900 sekund)
                current_session.append(timestamps[i])
            else:
                session_intervals.append(current_session)
                current_session = [timestamps[i]]

        session_intervals.append(current_session)
        session_results[ip] = session_intervals

    return session_results

# Wywołanie funkcji i zapis wyniku do pliku
result = identify_sessions(FILE_SRC_PATH)
with open(FILE_DEST_PATH, 'w') as input_file:
    for ip, sessions in result.items():
        input_file.write(f"IP: {ip}\n")
        for idx, session in enumerate(sessions, start=1):
            input_file.write(f"Session {idx}: {session[0]} - {session[-1]}\n")
        input_file.write("\n")

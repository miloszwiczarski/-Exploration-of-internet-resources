from collections import defaultdict
from pathlib import Path

FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")
FILE_DEST_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\output\requests_in_session.txt")


from collections import defaultdict


with open(FILE_SRC_PATH, 'r') as file:
    logs = file.readlines()


sessions = defaultdict(list)


session_length = 10  


for log in logs:
    log_parts = log.split(' ')
    ip_address = log_parts[0]
    timestamp = log_parts[3][1:]  
    sessions[ip_address].append(timestamp)


total_requests = 0
for ip, timestamps in sessions.items():
    num_requests = len(timestamps) // session_length
    total_requests += num_requests

average_requests_per_session = total_requests / len(sessions)


print(f"Średnia liczba żądań w sesji: {average_requests_per_session}")





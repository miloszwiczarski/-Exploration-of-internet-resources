from pathlib import Path
import re
from datetime import datetime
import matplotlib.pyplot as plt


FILE_SRC_PATH = Path(r"C:\Users\mwicz\OneDrive\Dokumenty\lab3\-Exploration-of-internet-resources\lab3\input\cleaned_apache_logs.txt")
with open(FILE_SRC_PATH, 'r') as file:
    lines = file.readlines()


# Wyrażenie regularne do ekstrakcji czasu
pattern = r'\[(\d{2}/\w+/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})\]'

# Zbieranie czasów wizyt
visit_times = []
session_times = []

for line in lines:
    match = re.search(pattern, line)
    if match:
        timestamp_str = match.group(1)
        timestamp = datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S %z")
        visit_times.append(timestamp)

# Obliczanie średniego czasu wizyty
if visit_times:
    total_visit_time = sum([(visit_times[i + 1] - visit_times[i]).total_seconds() for i in range(len(visit_times) - 1)])
    average_visit_time = total_visit_time / (len(visit_times) - 1)
    print(f"Średni czas wizyty: {average_visit_time:.2f} sekund")


visit_intervals = [(visit_times[i + 1] - visit_times[i]).total_seconds() for i in range(len(visit_times) - 1)]

plt.figure(figsize=(10, 6))
plt.hist(visit_intervals, bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram czasów wizyt')
plt.xlabel('Czas pomiędzy wizytami (sekundy)')
plt.ylabel('Liczba wizyt')
plt.grid(True)
plt.show()

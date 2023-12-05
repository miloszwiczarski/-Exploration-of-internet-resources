"""
Identyfikacja sesji użytkownika na podstawie logów serwera HTTP może być zrealizowana poprzez analizę czasu pomiędzy kolejnymi żądaniami (requestami) z tego samego adresu IP i przypisanie ich do jednej sesji. Istnieje wiele sposobów na zdefiniowanie sesji użytkownika w oparciu o logi serwera, a poniżej przedstawiony jest prosty algorytm opierający się na odstępie czasowym pomiędzy żądaniami.

Założenia algorytmu:

Sesja będzie traktowana jako seria żądań z tego samego adresu IP, w których odstępy czasowe pomiędzy żądaniami nie przekraczają pewnego ustalonego limitu czasowego (np. 30 minut).
Algorytm do identyfikacji sesji użytkownika na podstawie logów access.log:

Odczytaj logi z pliku access.log.

Posortuj logi chronologicznie.

Iteruj przez posortowane logi:

a. Dla każdego wpisu w logu:

b. Sprawdź, czy adres IP jest już znany jako aktywna sesja:

 - Jeśli tak, sprawdź różnicę czasu między bieżącym żądaniem a ostatnim żądaniem w sesji.
 
     - Jeśli różnica czasu jest mniejsza niż ustalony limit czasowy, dodaj bieżące żądanie do istniejącej sesji tego użytkownika.
     
     - Jeśli różnica czasu przekracza limit czasowy, zacznij nową sesję dla tego adresu IP.
 
 - Jeśli nie, rozpocznij nową sesję dla tego adresu IP i dodaj bieżące żądanie do nowej sesji.
Po zakończeniu iteracji przez logi, uzyskasz zestaw sesji dla poszczególnych adresów IP.

Poniżej znajduje się przykładowy algorytm w języku Python, który ilustruje powyższe kroki:
"""

from datetime import datetime, timedelta

# Odczyt logów z pliku access.log
with open('apache_logs.txt', 'r') as file:
    lines = file.readlines()

# Sortowanie logów chronologicznie
sorted_logs = sorted(lines, key=lambda x: datetime.strptime(x.split('[')[1].split(']')[0], '%d/%b/%Y:%H:%M:%S %z'))

# Definicja limitu czasowego dla sesji (30 minut)
session_timeout = timedelta(minutes=30)

# Słownik przechowujący sesje dla poszczególnych adresów IP
sessions = {}

# Iteracja przez posortowane logi
for log in sorted_logs:
    ip_address = log.split()[0]
    timestamp = datetime.strptime(log.split('[')[1].split(']')[0], '%d/%b/%Y:%H:%M:%S %z')
    
    # Sprawdzenie istniejącej sesji dla adresu IP
    if ip_address in sessions:
        last_request_time = sessions[ip_address][-1]['timestamp']
        time_difference = timestamp - last_request_time
        
        # Dodanie żądania do istniejącej sesji
        if time_difference <= session_timeout:
            sessions[ip_address].append({'timestamp': timestamp, 'request': log})
        # Rozpoczęcie nowej sesji
        else:
            sessions[ip_address] = [{'timestamp': timestamp, 'request': log}]
    # Rozpoczęcie nowej sesji dla adresu IP
    else:
        sessions[ip_address] = [{'timestamp': timestamp, 'request': log}]

# Tworzenie pliku z analizą sesji
with open('sesje_uzytkownikow.txt', 'w') as output_file:
    for ip, session in sessions.items():
        output_file.write(f"Sesja dla adresu IP {ip}:\n")
        for request in session:
            output_file.write(f"{request['request']}\n")
        output_file.write("\n")

    # Dodanie analizy sesji do pliku
    output_file.write("\n\n*** Analiza sesji użytkowników ***\n\n")
    output_file.write("Liczba sesji dla poszczególnych użytkowników:\n")
    for ip, session in sessions.items():
        output_file.write(f"Adres IP: {ip}, Liczba sesji: {len(session)}\n")

# 2 -----------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Algorytm iteruje przez logi, grupując żądania z tego samego adresu IP w sesje na podstawie odstępów czasowych między nimi. 
Każda sesja jest przechowywana jako lista żądań dla danego adresu IP. 
"""

# 3 -----------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Został przyjęty czas 30 minut jako limit czasowy dla sesji. 
Wybór czasu identyfikacji sesji jest istotny i zależy od charakteru działalności na stronie internetowej oraz oczekiwań dotyczących definicji sesji.

Czas identyfikacji sesji jest kwestią względną i może być dostosowany do konkretnych potrzeb. Oto kilka czynników, które należy wziąć pod uwagę:
Aktywność użytkowników: W przypadku częstej interakcji z treściami na stronie, dłuższa sesja może uwzględnić całą aktywność.
Bezpieczeństwo: Krótszy czas sesji może być lepszy dla ochrony informacji poufnych, ograniczając czas potencjalnego dostępu dla nieautoryzowanych osób.
Analiza danych: Dłuższe sesje ułatwiają lepsze zrozumienie nawyków użytkowników.
Doświadczenie użytkownika: Zbyt krótki czas sesji może być uciążliwy dla użytkowników, zwłaszcza podczas dłuższego przeglądania lub interakcji z zawartością strony.
Ostatecznie, optymalny
"""

# 4 -----------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Zakończenie sesji na stronie internetowej można określić na różne sposoby:

Brak aktywności: Sesję można zakończyć, gdy użytkownik przez dłuższy czas nie wykazuje żadnej aktywności.

Automatyczne wylogowanie: Użytkownik może zostać wylogowany po określonym czasie nieaktywności.

Specyficzne akcje: Potwierdzenie opuszczenia strony lub wykonanie określonej akcji może kończyć sesję.

Analiza zachowania: Badanie nawyków użytkowników pomaga określić moment zakończenia sesji.

Użycie ciasteczek: Informacje w ciasteczkach mogą wskazywać czas ostatniej aktywności.

Śledzenie ruchu: Monitorowanie zachowania użytkownika pomaga ustalić koniec sesji.
"""

# 5 -----------------------------------------------------------------------------------------------------------------------------------------------------------------



# 6 -----------------------------------------------------------------------------------------------------------------------------------------------------------------



# 7 -----------------------------------------------------------------------------------------------------------------------------------------------------------------



# 8 -----------------------------------------------------------------------------------------------------------------------------------------------------------------



# 9 -----------------------------------------------------------------------------------------------------------------------------------------------------------------


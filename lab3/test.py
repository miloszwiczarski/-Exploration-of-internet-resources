import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Odczyt logów z pliku cleaned_apache_logs.txt
with open('cleaned_apache_logs.txt', 'r') as file:
    lines = [next(file) for _ in range(859)]  # Odczytaj tylko pierwsze 1000 linii


# Przetworzenie danych logów
logs_list = [[line.split()[11]] for line in lines]
print(logs_list)
# Tworzenie ramki danych dla transakcji
te = TransactionEncoder()
te_ary = te.fit_transform(logs_list)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Wyszukiwanie częstych zbiorów
frequent_itemsets = apriori(df, min_support=0.1, use_colnames=True)

# Generowanie reguł asocjacyjnych
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.5)

# Zapis wyników do pliku
with open('analiza_regul_asocjacyjnych.txt', 'w') as output_file:
    output_file.write("Analiza reguł asocjacyjnych na podstawie logów:\n\n")
    output_file.write("Częste zbiory:\n")
    output_file.write(str(frequent_itemsets) + "\n\n")
    output_file.write("Reguły asocjacyjne:\n")
    output_file.write(str(rules))

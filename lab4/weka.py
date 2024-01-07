import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
import re
import arff

# Wczytanie danych z pliku .arff
data_path = 'Output.arff'
with open(data_path, 'r', encoding='utf-8') as f:
    data_generator = arff.load(f)
    data = list(data_generator)
    attributes = [attr[0] for attr in data[1]['attributes']]
    data_values = data[1]['data']
    df = pd.DataFrame(data_values, columns=attributes)

# Funkcja do usunięcia zbędnych termów
def remove_terms(text):
    unnecessary_terms = ['the', 'of', 'and', 'in', 'to', 'a', 'is', 'are', 'that', 'for', 'with', 'on', 'by', 'as']
    text = re.sub(r'\b(?:%s)\b' % '|'.join(unnecessary_terms), '', text)
    return text

# Pipeline przetwarzania danych
pipeline = Pipeline([
    ('string_to_word_vector', CountVectorizer(tokenizer=lambda text: text.split(), binary=True)),
])

# Wykonanie przekształceń
df_processed = pipeline.fit_transform(df['document_name'])

# Utworzenie DataFrame dla przekształconych danych
df_processed = pd.DataFrame(df_processed.toarray(), columns=pipeline.named_steps['string_to_word_vector'].get_feature_names_out())

# Usunięcie zbędnych termów
df_processed = df_processed.applymap(remove_terms)

# Zapis do pliku CSV
df_processed.to_csv('Department_terms_2.csv', index=False)

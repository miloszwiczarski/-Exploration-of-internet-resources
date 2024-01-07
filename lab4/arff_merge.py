import os

INPUT_DIR = r'C:\Users\mwicz\OneDrive\Dokumenty\Eksploracja zasobow internetowych\lab4\CCSU departments'

# Tworzenie listy plików w katalogu
files = os.listdir(INPUT_DIR)

with open('output.arff', 'w') as output_file:

    output_file.write('@relation departments_string\n\n')
    output_file.write('@attribute document_name string\n')
    output_file.write('@attribute document_content string\n\n')
    output_file.write('@data\n')
    
  
    for file_name in files:
       
        if file_name.endswith('.txt'):
            full_path = os.path.join(INPUT_DIR, file_name)
  
            with open(full_path, 'r') as file:
                content = file.read().replace('\n', ' ').replace('"', '\\"')  # Parsowanie
                content = ' '.join(content.split())  # Usuwanie spacji
                output_file.write(f'{file_name.replace(".txt", "")}, "{content}"\n')

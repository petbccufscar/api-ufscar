import csv

# Arquivos de entrada e saída
filtered_courses_file = 'filtered_courses.csv'
grades_file = 'grades.csv'
output_file = 'filtered_grades.csv'

# Coletar os códigos do arquivo filtered_courses.csv
codes = set()
with open(filtered_courses_file, mode='r', encoding='utf-8') as infile:
    reader = csv.reader(infile, delimiter=';')
    for row in reader:
        codes.add(row[-1])  # O código é o último atributo da linha

# Filtrar o arquivo grades.csv baseado nos códigos coletados
with open(grades_file, mode='r', encoding='utf-8') as infile, \
     open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
    
    reader = csv.reader(infile, delimiter=';')
    writer = csv.writer(outfile, delimiter=';')
    
    for row in reader:
        if row[0] in codes:  # O código é o primeiro atributo da linha
            writer.writerow(row)

print(f'Linhas filtradas do grades.csv foram salvas em {output_file}.')
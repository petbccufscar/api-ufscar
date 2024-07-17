import csv

input_file = 'all_courses.csv'
output_file = 'filtered_courses.csv'
keyword = 'UFSCAR'

with open(input_file, mode='r', encoding='utf-8') as infile, \
     open(output_file, mode='w', encoding='utf-8', newline='') as outfile:

    reader = csv.reader(infile, delimiter=';')
    writer = csv.writer(outfile, delimiter=';')
    
    for row in reader:
        if any(keyword in cell for cell in row):
            writer.writerow(row)

print(f'Linhas que contêm "{keyword}" foram filtradas e salvas em {output_file}.')
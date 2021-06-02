# removes instances from instancedata that were added recently
# we don't have currently this instances

import csv
import os

rel_path = 'tests\\examples\\minlplib2'
root_name = os.path.dirname(os.getcwd())
while True:
    base = os.path.basename(root_name)
    if base == 'decogo':
        break
    else:
        root_name = os.path.dirname(root_name)

dirname = os.path.join(root_name, rel_path)

files = [os.path.splitext(filename)[0] for filename in os.listdir(dirname)]
files.remove('__init__')
files.remove('__pycache__')

with open('instancedata.csv', 'r') as inp, open('instancedata_updated.csv', 'w', newline='') as out:
    reader = csv.DictReader(inp, delimiter=';')
    writer = csv.DictWriter(out, fieldnames=reader.fieldnames, delimiter=';')
    writer.writeheader()

    files.sort()

    i = 0
    for row in reader:
        if row['name'] == files[i]:
            writer.writerow(row)
            i += 1

inp.close()
out.close()
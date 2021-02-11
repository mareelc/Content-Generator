# Laura Maree

import sys
import csv
from verify_search import *

def read_csv():
    keywords = []
    with open(sys.argv[1], newline="") as file:
        read = csv.reader(file, delimiter=' ', quotechar='|')
        for row in read:
            for word in row:
                keywords.append(word)
    keywords = keywords[1]
    keys = keywords.split(';')
    results = verify_keywords(keys[0], keys[1])
    write_csv(keys, results)

def write_csv(keywords, results):
    with open('output.csv', 'w', encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        keys = ';'.join(keywords)
        csv_writer.writerow(["input_keywords", "output_content"])
        row = [keys, results[1]]
        csv_writer.writerow(row)
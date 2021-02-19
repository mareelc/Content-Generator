# Laura Maree
# Read/Write csv
# 2.12.2021

import sys
import csv
from verify_search import *

def read_csv():
    """Read csv file from command line. Immediately
    call to find wiki paragraph with both keywords
    and write to file."""
    keywords = []

    with open(sys.argv[1], newline="") as file:
        read = csv.reader(file, delimiter=' ', quotechar='|')
        for row in read:
            for word in row:
                keywords.append(word)
    keywords = keywords[1]
    keys = keywords.split(';')
    write_csv(keys, verify_keywords(keys[0], keys[1]))

def write_csv(keywords, results):
    """Write results to output.csv."""
    with open('output.csv', 'w', encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        keys = ';'.join(keywords)
        # Column headers
        csv_writer.writerow(["input_keywords", "output_content"])

        # Messages for errors
        if not results[1]:
            results[1] = "Paragraph not found."
        if type(results) == str:
            csv_writer.writerow([keys, results])
        # Results for paragraph/disambig.
        else:
            csv_writer.writerow([keys, results[1]])
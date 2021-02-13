# Laura Maree
# Read/Write csv
# 2.12.2021

import sys
import csv
from verify_search import *

def read_csv():
    """
    Read csv file from command line. Immediately
    call to find wiki paragraph with both keywords
    and write to file.
    :return: None.
    """
    keywords = []
    # Read file and save keywords.
    with open(sys.argv[1], newline="") as file:
        read = csv.reader(file, delimiter=' ', quotechar='|')
        for row in read:
            for word in row:
                keywords.append(word)
    keywords = keywords[1]
    keys = keywords.split(';')

    # Call to verify keys and search wiki.
    results = verify_keywords(keys[0], keys[1])
    # Write results
    write_csv(keys, results)

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
            row = [keys, results]
        # Results for paragraph/disambig.
        else:
            row = [keys, results[1]]
        csv_writer.writerow(row)
# Laura Maree
# Content_Generator.py
# 2.12.2021

import sys
import gui
import read_write

def check_for_csv():
    """Check if csv file present at start."""
    # Run with file and call to read file.
    if len(sys.argv) > 1:
        read_write.read_csv()
    # Run without csv input file.
    else:
        gui.main()

def main():
    """Main function for http_server.py."""
    check_for_csv()

if __name__ == '__main__':
    main()
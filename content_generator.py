# Laura Maree

import sys
import gui
import read_write

def check_for_csv():
    if len(sys.argv) > 1:
        read_write.read_csv()
    else:
        gui.main()

def main():
    """Main function for http_server.py."""
    check_for_csv()

if __name__ == '__main__':
    main()
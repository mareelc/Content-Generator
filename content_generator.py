# heinl11
# content_generator.py
# 3.10.2021

import sys
import gui
import read_write
import listen
import send

def check_for_comms():
    """Check for incoming communication from Life Generator."""
    paragraph = listen.listening()
    return paragraph

def check_for_csv():
    """Check if csv file present at start."""
    # Run with file and call to read file.
    if len(sys.argv) > 1:
        read_write.read_csv()
    # Run without csv input file.
    else:
        gui.main()

def main():
    """Main function for content_generator.py."""
    # If incoming communication, send second request.
    paragraph = check_for_comms()
    if paragraph:
        send.sending()
        return

    check_for_csv()

if __name__ == "__main__":
    main()

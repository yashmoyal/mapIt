#!python3
# mapIt.py- launches a map in the browser using an address from the clipboard or command line.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # get address from the command line.
    address = ''.join(sys.argv[1:])
else:
    # get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + address)
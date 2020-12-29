# Covid-Monitor
A simple python script to handle a visitor record. Both CLI and GUI (using PySimpleGUI)

Dependencies: Python 3, PySimpleGUI (https://github.com/PySimpleGUI/PySimpleGUI)

The variable 'registro' sets the path to the .csv file where records are stored.

This version is designed to work on Windows systems, with the record file stored in a network smb share, it needs to be modified in order to work with other systems.

I built it with PyInstaller to run as a single file in windowed mode.

Usage:
Write visitor name and phone number, confirm with yes and the record will be appended to the .csv file.
CLose or click exit to terminate

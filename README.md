# Covid-Monitor
A simple python script to handle a visitor record. Both CLI and GUI (using PySimpleGUI)

Dependencies: Python 3

The variable 'registro' sets the path to the .csv file where records are stored.

This version is designed to work on Windows systems, with the record file stored in a network smb share, it needs to be modified in order to work with other systems.

I run this script directly from cmd.

Usage:
Write visitor name and phone number sonfirming each one by pressing enter.
The record is appended to the .csv file.
Close terminal or press ctrl+c to exit.

Each line is made up by time of record, name of the pc (in order to identify the office) and the data entered by user.

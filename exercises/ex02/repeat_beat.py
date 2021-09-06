"""Repeating a beat in a loop."""

USERBEAT = input("What beat do you want to repeat? ")
USERREPEAT = int(input("How many times do you want to repeat it? "))

if USERREPEAT >= 1:
    SONG = (USERBEAT + " ") * USERREPEAT
    print(SONG)
else: 
    print("No beat...")



__author__ = "730358517"

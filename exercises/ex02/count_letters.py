"""Counting letters in a string."""

WHATLETTER = input("What letter do you want to search for? ")
ENTERWORD = input("Enter a word: ")
COUNT = 0
n = len(ENTERWORD)
i = 0
while i < n:
    if ENTERWORD[i] == WHATLETTER:
        COUNT = COUNT + 1
    i += 1
print("Count: ", COUNT)

_author_ = "730358517"
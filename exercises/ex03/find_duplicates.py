"""Finding duplicate letters in a word."""

UserWord = input("Enter a word:")

i = 0
p = 0
duplicate = 0
end = len(UserWord) - 1

while i < end:
    while p <= (end - 1): 
        if UserWord[i] == UserWord[p + 1]:
            duplicate = (duplicate + 1)
        p = p + 1
    i = i + 1
    p = i
if duplicate > 0:
    print("Found duplicate:", True)
else:
    print("Found duplicate:", False)

__author__ = "123456789"

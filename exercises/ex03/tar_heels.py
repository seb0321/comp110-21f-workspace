"""An exercise in remainders and boolean logic."""

UserInt = int(input("Enter an int:"))

if UserInt % 2 == 0 and UserInt % 7 != 0:
    print("TAR")
if UserInt % 7 == 0 and UserInt % 2 != 0: 
    print("HEELS")
if UserInt % 7 == 0 and UserInt % 2 == 0:
    print("TAR HEELS")
else:
    print("CAROLINA")

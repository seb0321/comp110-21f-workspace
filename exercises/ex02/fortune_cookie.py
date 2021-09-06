"""Fortune Cookie Generator."""
from random import randint

print("Your fortune cookie says...")
RANDOMINTEGER = randint(1, 4)

if RANDOMINTEGER >= 1:
    if RANDOMINTEGER == 1:
        print("You are beautiful on the inside and out.")
    else:
        if RANDOMINTEGER == 2:
            print("Don't just think, act!")
        else:
            if RANDOMINTEGER == 3:
                print("A lifetime friend will soon be made.")
            else: 
                if RANDOMINTEGER == 4:
                    print("All your hardwork will pay off.")

print("Now, go spread positive vibes!")


_author_ = "730358517"
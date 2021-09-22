"""Choose your own adventure!"""
import random

points: int = 0
HILARIOUS = "\U0001F923"
BAD = "\U0001F643"
GOOD = "\U0001F607"
PLANT = "\U0001F331"
SHOCKED = "\U0001F631"
cactus = 0
player: str = ""
plant = 0
count = 0


def greet() -> None:
    global player 
    player = input("What is your name? ")
    print(f"Welcome to your virtual garden, {player}!")
    print("In this game you will follow prompts and try not to kill your plants. If you get 500 adventure points, you win! Have fun!!")


def CactusFunc(a):
    global points 
    global cactus 
    global plant
    cactus_input = int(input("How many cups of water? Enter the number of cups: "))
    if cactus_input > 1:
        print(HILARIOUS, "You killed a cactus. Try again.")
        a = 0
        cactus = cactus - 1
        if cactus == 0 and plant == 0:
            print("All your plants are dead.")
            take_care(-500)
        else: 
            CactusFunc(a)
    elif a > 300: 
        a = 0
        cactus = 0
        plant = plant - cactus
        print("You no longer have any cacti and your adventure points are 0.")
        take_care(a)
    else: 
        print("Great job! Plus 200 adventure points!")
        a = a + 200
        print(f"You have {a} adventure points")
        take_care(a)


def YesNoFunc():
    Yes_No = input("Yes or No? ")
    Yes_No = Yes_No.lower()
    if Yes_No == "yes":
        return "yes"
    else: 
        return "no"


def plant_shopping():
    global player 
    global points
    global cactus
    global plant 
    player_input = input("What plant do you want to buy? \n 1. A snake plant \n 2. A cactus \n 3. A pothos \n 4. Fake plant \n Enter name of the plant: ")
    player_input = player_input.lower()
    if plant < 6 or plant == 0:
        if player_input == ("snake plant" or "a snake plant"):
            plant = plant + 1
            print(f"That is a great choice, {player}, almost impossible to kill! Plus 5 points!")
            points = points + 5
            print(f"Would you like to take care of it {player}? (no = buy another plant)")
            YesNo = YesNoFunc()
            if YesNo == "yes":
                points = points + 10
                print(GOOD, PLANT, "Plus 10 points!")
                points = take_care(points)
            else:
                print(f"Would you like to buy another plant {player}?")
                YesNo = YesNoFunc()
                if YesNo == "yes":
                    plant_shopping()
                else:
                    points = points - 10
                    print(BAD, "Minus 10 adventure points.")
                    print(f"{BAD}, minus 10 adventure points. You have {points} adventure points. Thanks for playing, goodbye!")
        elif player_input == "cactus" or player_input == "a cactus":
            plant = plant + 1
            points = 3
            cactus = cactus + 1
            print("Be careful! Don't water too much!! Plus 3 adventure points!")
            print(f"Would you like to take care of it {player}? (No = buy another plant)")
            YesNo = YesNoFunc()
            if YesNo == "yes":
                points = points + 10
                print(GOOD, PLANT, "Plus 10 adventure points!")
                points = take_care(points)
            else: 
                print(f"Would you like to buy another plant {player}?")
                YesNo = YesNoFunc()
                if YesNo == "yes":
                    plant_shopping()
                else:
                    points = points - 10
                    print(BAD, "Minus 10 adventure points.")
                    print(f"{BAD}, minus 10 adventure points. You have {points} adventure points. Thanks for playing, goodbye.")
        elif player_input == "pothos" or player_input == "a pothos":
            plant = plant + 1
            points = points + 10
            print("That's a great choice! They are super easy to take care of! Plus 10 adventure points!")
            print(f"Would you like to take care of it {player}? (no = buy another plant)")
            YesNo = YesNoFunc()
            if YesNo == "yes":
                points = points + 10
                print(GOOD, PLANT, "Plus 10 adventure points!")
                points = take_care(points)
            else: 
                print(f"Would you like to buy another plant {player}?")
                YesNo = YesNoFunc()
                if YesNo == "yes":
                    plant_shopping()
                else:
                    points = points - 10
                    print(f"{BAD}, minus 10 adventure points. You have {points} adventure points. Thanks for playing, goodbye.")
        elif player_input == "fake plant":
            plant = plant + 1
            points = points - 150
            print("Minus 150 adventure points and go buy another plant.", HILARIOUS)
            plant_shopping()
        else: 
            print("Oops! Make sure you spelt your entry correctly and/or capitalized properly.")
            plant_shopping()
    else:
        Too_Many = input("Oops! You can't buy more plants. Would you like like to \n a. stop playing \n b.take care of your plant? \n Enter a or b:")
        if Too_Many == "a":
            print(f"Thank you for playing, goodbye! You have {points} adventure points")
            points = 0
        else:
            points = take_care(points)


def take_care(p):
    global cactus 
    global plant
    global count
    if p == 0:
        print("You need to buy some plants!")
        plant_shopping()
    while p > 0:
        if p > 500:
            print(f"Yay you're a great plant parent! You won{GOOD}! You had {p} points")
            exit()
        count = count + 1
        if count == 4: 
            print("Proceed with caution.")
        if count % 5 == 0:
            p = p - (75 * plant)
            count = 0
            print(SHOCKED, "You lost 75 adventure points per plant for giving your plant(s) too much love! You have", p, "points.")
            take_care(p)
        print(f"Yay! Your adventure points are in the positive {GOOD}")
        player_input = int(input("Do you want to: \n 1. Water your plant \n 2. Remove dead leaves \n 3. Fertilize \n 4. Leave game \n Enter a number: "))
        if player_input == 1:
            if cactus >= 1:
                CactusFunc(p)
            else: 
                WaterPoints = random.randint(-50, 20)
                p = p + (WaterPoints * plant)
                print(f"{player}, you got {WaterPoints} per plant. You now have {p}")
        elif player_input == 2: 
            p = p + (10 * plant)
            print(f"You now have {p} points!")
        elif player_input == 3: 
            Fertilizer = random.randint(0, 1)
            if Fertilizer == 1: 
                p = p + (10 * plant)
                print("You got 10 adventure points per plant! You have", p, "points!")
            else: 
                p = p - (plant * 20)
                print("You got a bad fertilizer! Minus 20 per plant.")
                print(f"You have {p} points.")
        else: 
            print(f"Bye, you had {p} points! Thanks for playing.")
            exit()
    while p <= 0:
        if p < -500: 
            print(f"{player}, your plants have DIED {HILARIOUS} {BAD}. Try again.")
            plant = 0
            p = 0
            return p
        print(SHOCKED, "OH NO! You have negative adventure points!! You better start taking better care of your ", PLANT, "!")
        player_input = int(input("Do you want to: \n 1. Water your plant \n 2. Remove dead leaves \n 3. Fertilize \n 4. Leave game \n Enter a number: "))
        if player_input == 1:
            if cactus >= 1:
                CactusFunc(p)
            else: 
                WaterPoints = random.randint(0, 50)
                p = p + (WaterPoints * plant)
                print(f"{player}, you got {WaterPoints} adventure points per plant. You now have {p} adventure points")
        elif player_input == 2: 
            p = p + (15 * plant)
            print(f"You now have {p} adventure points!")
        elif player_input == 3: 
            Fertilizer = random.randint(0, 1)
            if Fertilizer == 1: 
                p = p + (5 * plant) 
                print(f"You got {p} adventure points!")
            else: 
                p = p - (10 * plant)
                print("You got a bad fertilizer.")
                print(f"You have {p} adventure points")
        else: 
            print(f"Bye, you had {p} adventure points. Thanks for playing!")
            exit()
    return p


def main() -> None:
    global points 
    global cactus 
    global plant
    print("Hello! Welcome to your garden!")
    greet()
    player_input = int(input("You have 3 choices \n 1. Do you want to go plant shopping. \n 2. Take care of your plants. \n 3. Go home. \n Enter corresponding number: "))
    if player_input == 1:
        plant_shopping() 
    if player_input == 2:
        points = take_care(points)
    else:
        print("Thank you for playing, goodbye!")
        if points < 0:
            print(f"You haven {points} adventure points {BAD}")
            points = 0
            plant = 0
        elif points > 0:
            print(f"You have {points} adventure points {GOOD}")
            points = 0
            plant = 0
        else:
            print(f"You have {points} adventure points")
            points = 0
            plant = 0


if __name__ == "__main__":
    main()


__author__ = "730358517"
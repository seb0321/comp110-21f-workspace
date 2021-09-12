"""Drawing forests in a loop."""


USERTREE = int(input("Depth: "))
TREE: str = '\U0001F332'
i = 1

while USERTREE >= 1:
    FOREST = TREE * i
    print(FOREST) 
    USERTREE = USERTREE - 1
    i = i + 1

__author__ = "730358517"

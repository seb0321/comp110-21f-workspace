"""List utility functions."""


def all(intlist, number) -> bool:
    i: int = 0 
    while i < len(intlist):
        if intlist[i] != number:
            return False
        i += 1
    return True


def is_equal(numberlist, numbercatalog) -> bool:
    i: int = 0 
    while i < len(numberlist):
        if numberlist[i] != numbercatalog:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    m = input[0]
    i = 0
    while i < len(input):
        if input[i] < m:
            m = input[i]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    return m 
    
        
def main():
    print(all([1, 2, 3], 1))
    print(all([1, 1, 1], 2))
    print(all([1, 1, 1], 1))

    print(is_equal([1, 0, 1], [1, 0, 1]))
    print(is_equal([1, 1, 0], [1, 0, 1]))

    print(max([1, 3, 2]))
    print(max([100, 99, 98]))
    print(max([]))


if __name__ == "__main__":
    main()

__author__ = "730358517"


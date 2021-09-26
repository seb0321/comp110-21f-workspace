"""List utility functions."""


def all(intlist: list, number: int) -> bool:
    """All function."""
    i: int = 0 
    if len(intlist) == 0:
        return False
    while i < len(intlist):
        if intlist[i] != number:
            return False
        i += 1
    return True


def is_equal(numberlist: list[int], numbercatalog: list[int]) -> bool:
    """Equal function."""
    if len(numbercatalog) != len(numberlist):
        return False
    i: int = 0 
    while i < len(numberlist):
        if numberlist[i] != numbercatalog[i]:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Max function."""
    m: int = input[0]
    i: int = 0
    while i < len(input):
        if input[i] > m:
            m = input[i]
            i += 1
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    return m
    
        
def main():
    """Main Function."""
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


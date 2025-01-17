"""List utility functions."""


def only_evens(input: list[int]) -> list[int]:
    """Max function."""
    m: int = 0
    i: int = 0
    twos = list()
    while i < len(input):
        m = input[i]
        if m % 2 == 0:
            twos.append(m)
        i += 1
    return twos


def sub(a_list: list[int], a: int, b: int) -> list[int]:
    """Sub Function."""
    if len(a_list) == 0:
        return []
    if a > b:
        return []
    if a < 0:
        a = 0
    if b > len(a_list):
        b = len(a_list)
    index = list()
    for x in range(a, b):
        index.append(a_list[x])
    
    return index


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Concat Function."""
    newlist = list_one + list_two
    return newlist
     
    
def main() -> None:
    """Main Function."""
    print(only_evens([1, 2, 3]))
    print(only_evens([1, 5, 3]))
    print(only_evens([4, 4, 4]))
    print(sub([10, 20, 30, 40], 1, 3))


if __name__ == "__main__":
    main()


__author__ = "730358517"
"""Practice with dictionaries."""


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert Function."""
    emptydict: dict[str, str] = {}

    for a in input:
        if input[a] in emptydict: 
            raise KeyError("You have an error.")
        emptydict[input[a]] = a
    return emptydict
    
    
def favorite_color(color: dict[str, str]) -> str:
    """Favorite Color Function!"""
    max = 0
    curr = 0
    for a in color:
        for b in color:
            if color[a] == color[b] and a != color[b]:
                curr += 1      
        if curr > max:
            maxkey = color[a]
            max = curr
        curr = 0
    return maxkey
    

def count(input: list[str]) -> dict[str, int]:
    """Count Function."""
    counter = dict()
    for a in input:
        counter[a] = 0
    for a in counter.keys():
        for b in input:
            if b == a:
                counter[a] = counter[a] + 1
    return counter


def main() -> None:
    """Main Function."""


print(count(['sarah', 'sam', 'sarah']))


if __name__ == "__main__":
    main()


__author__ = "730358517"
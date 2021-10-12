"""Practice with dictionaries."""


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert Function."""
    for a in input.keys():
        for b in input.keys():
            if input[a] == input[b] and a != b: 
                raise KeyError("You have an error.")
    for i in input.keys():
        input[input[i]] = i
        input.pop(i)
    return input
    
    
def favorite_color(color: dict[str, str]) -> str:
    """Favorite Color Function!"""
    max = 0 
    curr = 0
    for a in color.keys():
        for b in color.keys():
            if color[a] == color[b] and a != b:
                curr += 1      
        if curr > max:
            maxkey = a
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
            if list(b) == a:
                counter[a] = counter[a] + 1
    return counter


__author__ = "730358517"
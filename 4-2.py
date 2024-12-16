import re

A = re.compile(r'A')

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def loadInput() -> list[str]:
    return open("4.txt").read().splitlines()

def findAllACoords(inputList: list[str]) -> list[Coords]:
    return [Coords(match.start(), y) for y, row in enumerate(inputList) for match in re.finditer(A, row)]

def findMatch(input: list[str], c: Coords):
    if not 0 < c.y < len(input)-1 or not 0 < c.x < len(input[c.y])-1: return False
    return isMS(input[c.y-1][c.x-1], input[c.y+1][c.x+1]) and isMS(input[c.y-1][c.x+1], input[c.y+1][c.x-1])

def isMS(string1: str, string2: str) -> bool:
    return string1+string2 in ["MS", "SM"]

def sumMatches(inputList: list[str], aCoords: list[Coords]) -> int:
    return sum(findMatch(inputList, coords) for coords in aCoords)

if __name__ == '__main__':
    inputList = loadInput()
    allACoords = findAllACoords(inputList)
    print(sumMatches(inputList, allACoords))
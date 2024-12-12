import re

A = re.compile(r'A')

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"Coords({self.x},{self.y})"

def loadInput() -> list[str]:
    return open("4.txt").read().splitlines()

def findAllACoords(inputList: list[str]) -> list[Coords]:
    return [Coords(match.start(), y) for y, row in enumerate(inputList) for match in re.finditer(A, row)]

def findMatch(inputList: list[str], coords: Coords):
    if not 0 < coords.y < len(inputList)-1 and not 0 < coords.x+1 < len(inputList[coords.y]): return False
    return 

if __name__ == '__main__':
    inputList = loadInput()
    allACoords = findAllACoords(inputList)
    print(allACoords)
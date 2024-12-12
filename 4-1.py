from typing import Iterator
import re

X = re.compile(r'X')
xmas = list("XMAS")

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

dirs = [
    Coords( 1,  1), # SE
    Coords( 1,  0), # E
    Coords( 1, -1), # NE
    Coords( 0, -1), # N
    Coords(-1, -1), # NW
    Coords(-1,  0), # W
    Coords(-1,  1), # SW
    Coords( 0,  1), # S
]

def findMatchRecursive(inputList: list[str], coords: Coords, dir: Coords, xIndex = 0) -> bool:
    if not 0 <= coords.y < len(inputList) or not 0 <= coords.x < len(inputList[coords.y]): return False
    if inputList[coords.y][coords.x] != xmas[xIndex]: return False
    if xIndex == 3: return True
    return findMatchRecursive(inputList, Coords(coords.x + dir.x, coords.y + dir.y), dir, xIndex + 1)

def loadInput() -> list[str]:
    return open("4.txt").read().splitlines()

def findAllXcoords(inputList: list[str]) -> Iterator[Coords]:
    return [Coords(match.start(), y) for y, row in enumerate(inputList) for match in re.finditer(X, row)]

def findMatch(inputList: list[str], start: Coords, dir: Coords) -> bool:
    if not 0 <= start.y + (dir.y * 3) < len(inputList) or not 0 <= start.x + (dir.x * 3) < len(inputList[start.y]): return False
    return [inputList[c.y][c.x] for c in [Coords(start.x + (dir.x * i), start.y + (dir.y * i)) for i in range(4)]] == xmas

def sumMatchesAllDirs(coordList: list[Coords]):
    return sum(findMatch(inputList, coords, dir) for coords in coordList for dir in dirs)

if __name__ == '__main__':
    inputList = loadInput()
    allXCoords = findAllXcoords(inputList)
    count = sumMatchesAllDirs(allXCoords)

    print(count)
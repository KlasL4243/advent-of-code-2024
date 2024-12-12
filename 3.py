import re
from typing import Iterator

patterns = {
    "mul": r"mul\([0-9]{1,3},[0-9]{1,3}\)",
    "do": r"do\(\)",
    "don't": r"don't\(\)"
}

def loadInput(path: str) -> str:
    return open(path).read()

def findMuls(string: str) -> list[str]:
    return re.findall(patterns["mul"], string)

def findDoMuls(string: str) -> list[str]:
    return re.findall('|'.join(patterns.values()), string)

def findNumPairs(stringList: list[str]) -> list[list[str]]:
    return [re.findall(r"[0-9]{1,3}", string) for string in stringList]

def evelMulSum(inputList: list[list[str]]) -> list[int]:
    return sum([int(pair[0]) * int(pair[1]) for pair in inputList])

def filterMuls(stringList: list[str]) -> Iterator[list[str]]:
    do = True
    for value in stringList:
        if value == "do()":
            do = True
        elif value == "don't()":
            do = False
        else:
            if do:
                yield value

if __name__ == '__main__':
    inputString = loadInput("3.txt")

    withoutDo = evelMulSum(findNumPairs(findMuls(inputString)))
    withDo = evelMulSum(findNumPairs(filterMuls(findDoMuls(inputString))))

    print(withoutDo)
    print(withDo)

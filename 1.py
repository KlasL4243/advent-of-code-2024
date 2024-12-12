liste1 = [3, 4, 2, 1, 3, 3]
liste2 = [4, 3, 5, 3, 9, 3]

def get2Lists(path: str) -> tuple[list[int], list[int]]:
    inputList = open(path).read().splitlines()
    splitted =  [line.split("   ") for line in inputList]

    list0 = [int(line[0]) for line in splitted]
    list1 = [int(line[1]) for line in splitted]

    return list0, list1

def getTotalDistanceFromInput(list0: list[int], list1: list[int]):
    return sum([abs(v1 - v0) for v0, v1 in zip(sorted(list0), sorted(list1))])

def getSimilaryScoreFromInput(list0: list[int], list1: list[int]) -> int:
    return sum([v0 * list1.count(v0) for v0 in list0])
        

if __name__ == '__main__':
    list0, list1 = get2Lists("1.txt")

    diffSum = getTotalDistanceFromInput(list0, list1)

    simSum = getSimilaryScoreFromInput(list0, list1)
    print(simSum)
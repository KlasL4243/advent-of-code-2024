def loadInput(path: str) -> list[list[int]]:
    return [[int(value) for value in liste] for liste in [line.split(' ') for line in open(path).read().splitlines()]]

def isIncreasing(report: list[list[int]]) -> list[bool]:
        return [1 <= report[index+1] - report[index] <= 3 for index in range(len(report)-1)]

def isDecreasing(report: list[list[int]]) -> list[bool]:
        return [1 <= report[index] - report[index+1] <= 3 for index in range(len(report)-1)]

def isDecreasingDampable(report: list[list[int]]) -> bool:
     isdecreasing = isDecreasing(report)
     badCount = isdecreasing.count(False)
     if (badCount == 0): 
          return True
     firstBad = isdecreasing.index(False)
     r = report.copy()
     r.pop(firstBad)

     return all(isDecreasing(r))

def isIncreasingDampable(report: list[list[int]]) -> bool:
     isincreasing = isIncreasing(report)
     badCount = isincreasing.count(False)
     if (badCount == 0): 
          return True
     firstBad = isincreasing.index(False)
     r = report.copy()
     r.pop(firstBad)

     return all(isIncreasing(r))


def isSaveList(reportList: list[list[int]]) -> list[bool]:
    return [(all(isIncreasing(report)) or all(isDecreasing(report))) for report in reportList].count(True)

def isDampdedSaveList(reportList: list[list[int]]) -> list[bool]:
    return [isDecreasingDampable(report) or isIncreasingDampable(report) for report in reportList].count(True)

if __name__ == '__main__':
    reportList = loadInput("2.txt")
    print(isSaveList(reportList))
    print(isDampdedSaveList(reportList))
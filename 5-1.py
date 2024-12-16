def loadInputs() -> tuple[list[list[int]]]:
    input = open("5.txt").read().splitlines()
    splitIndex = input.index('')

    rules = [[int(rule) for rule in line.split('|')] for line in input[0:splitIndex]]
    updates = [[int(update) for update in line.split(',')] for line in input[splitIndex+1:]]
    return rules, updates

def isSectionvalide(rules: list[list[int]], section: list[int]) -> bool:
    return all(section.index(rule[0]) < section.index(rule[1]) for rule in rules if all(value in section for value in rule))

def sumMidUpdateInValideSections(rules: list[int], updates: list[list[int]]) -> int:
    return sum(section[len(section)//2] for section in updates if isSectionvalide(rules, section))

if __name__ == '__main__':
    rules, updates = loadInputs()
    print(sumMidUpdateInValideSections(rules, updates))
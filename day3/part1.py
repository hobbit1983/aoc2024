import re

total = 0
regex = r"mul\((\d+),(\d+)\)"

def find_match(test_str: str):
    global total
    matches = re.finditer(regex, test_str, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        number1 = int(match.group(1))
        number2 = int(match.group(2))
        total = total + (number1 * number2)

with open("input") as file:
    find_match(file.read())
        
print(total)
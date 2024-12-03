import re

total = 0


def find_match(test_str: str):
    regex = r"mul\((\d+),(\d+)\)"
    global total
    matches = re.finditer(regex, test_str, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        number1 = int(match.group(1))
        number2 = int(match.group(2))
        total = total + (number1 * number2)


def remove_dont_statements(test_str: str) -> str:
    regex = r"don't\(\).*?do\(\)"
    return re.sub(regex,"",test_str,0,re.MULTILINE)

with open("input") as file:
    find_match(remove_dont_statements(file.read()))
        
print(total)
# 69402845 is too low
# 106414362 too high
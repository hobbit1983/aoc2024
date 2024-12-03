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
    # remove line breaks
    regex = r"\n"
    test_str = re.sub(regex," ",test_str,0,re.MULTILINE)
    # remove sections between a don't() and do()
    regex = r"don't\(\).*?do\(\)"
    test_str = re.sub(regex," ",test_str,0,re.MULTILINE)
    # remove trailing don't()
    regex = r"don't\(\).*"
    test_str = re.sub(regex," ",test_str,0,re.MULTILINE)
    return test_str

with open("input") as file:
    find_match(remove_dont_statements(file.read()))
        
print(total)

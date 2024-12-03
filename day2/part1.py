safe_reports = 0

def check_pair(a: int, b: int):
    if abs(int(a)-int(b)) <=3 :
        return True
    else:
        return False
    
def is_report_increasing(report: [int]) -> bool:
    for x in range(0, len(report)-1):
        if int(report[x]) < int(report[x+1]):
            continue
        else:
            return False
    return True

def is_report_dereasing(report: [int]) -> bool:
    for x in range(0, len(report)-1):
        if int(report[x]) > int(report[x+1]):
            continue
        else:
            return False
    return True
        
    
#Report is increasing or decreasing by at least 1 but a maximum of 3
def is_report_safe(report: [int]) -> bool:
    if is_report_increasing(report) or is_report_dereasing(report):
        for x in range(0,len(report)-1):
            if check_pair(int(report[x]), int(report[x+1])) == False:
                return False
        return True
    else:
        return False


with open("input") as file:
    while line := file.readline():
        if is_report_safe(line.split()):
            safe_reports += 1


print(safe_reports)
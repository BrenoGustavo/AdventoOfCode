import os
caminho_input = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputdia2.txt")
with open(caminho_input, 'r') as arquivo:
    reports_list = [[int(numero) for numero in lista.split()] for lista in arquivo.readlines()]


def is_increasing(report):
    cur_lev = report[0]
    for i in range(len(report)-1):
        if 3 >= (report[i+1] - cur_lev) >= 1:
            cur_lev = report[i+1]
        else:
            return False
    return True

def is_decreasing(report):
    cur_lev = report[-1]
    for i in range(len(report) -1 , 0, -1):
        if 3 >= (report[i-1] - cur_lev) >= 1:
            cur_lev = report[i-1]
        else:
            return False
    return True
        
def is_safe(report):
    return is_decreasing(report) or is_increasing(report)

safe_counts = 0
for report in reports_list:
    print(f'Safe counts atual: {safe_counts}')
    if is_safe(report):
        safe_counts +=1

print(safe_counts)

import os
input_txt = 'inputdia2.txt'
caminho_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), input_txt )
with open(caminho_txt, 'r') as arquivo:
    listed_reports = [[int(numero) for numero in linha.split()] for linha in arquivo.readlines()]

def is_safe(report: list):
    increasing = all(1 <= report[i+1] - report[i] <=3 for i in range(len(report)-1))
    decreasing = all(1 <= report[i] - report[i+1] <=3 for i in range(len(report)-1))
    return increasing or decreasing
def reactor_dumpener(report):

    if is_safe(report):  # If already safe, no need to remove anything
        return True

    for i in range(len(report)):
        cut_report = report[:i] + report[i+1:]
        if is_safe(cut_report):
            return True
        
    return False
    
contagem = 0
for report in listed_reports:

    if reactor_dumpener(report):
        contagem+=1

print(f'Safe reports: {contagem}')
        

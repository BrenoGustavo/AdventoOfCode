from pathlib import Path
import time
puzzle_input = Path(__file__).parent / 'inputday10.txt'

with open(puzzle_input, 'r') as archive:
    puzzle_input = archive.read()

# print(puzzle_input)

# 1122111 -> 212231

def contar(num:str):
    num += '!'
    num_list = list(num)
    new = []
    count = 0
    for i in range(len(num)):
        if i == 0:
            cur = num[i]
        
        if num[i] != cur:
            to_add = str(count) + cur
            new.append(to_add)
            cur = num[i]
            count = 1
        elif num[i] == cur:
            count +=1
    return ''.join(new)



def look_and_say(num, n):
    if n < 1:
        return num
    return look_and_say(contar(''.join(num)), n-1)

t1 = time.time()
result = look_and_say(puzzle_input, 50)
print(len(result))
print(time.time() - t1)

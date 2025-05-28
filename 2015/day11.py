#type: ignore
from pathlib import Path
import time
puzzle_input = Path(__file__).parent / 'inputday11.txt'
with open(puzzle_input, 'r') as archive:
    puzzle_input = archive.read()

def rule1(pw):

    for i in range(len(pw)-2):
        if ord(pw[i+2]) - ord(pw[i+1]) == ord(pw[i+1]) - ord(pw[i]) == 1:
            return True
    else:
        return False
    
def rule2(pw):
    for i in pw:
        if i in "ilo":
            return False
    return True

def rule3(pw):

    duos = set()
    for i in range(len(pw)-1):
        if pw[i] == pw[i+1]:
            duos.add(pw[i])
            if len(duos) >= 2:
                return True
    return False

def increment(s: str) -> str:
    if not s:
        return "a"
    
    s = list(s) #type: ignore
    i = len(s) - 1  
    
    while i >= 0:
        if s[i] == 'z':
            s[i] = 'a'  
            i -= 1  
        else:
            s[i] = chr(ord(s[i]) + 1) 
            return "".join(s)  
    
    return "a" + "".join(s)

# string = "vzbxkjhx"
# for i in range(2):
#     new = increment(string)
#     print(type(new))
#     print(new)
#     string = new

def next_pw(string):
  
    k = 0
    while True: 
        next_str = increment(string)
        if rule1(next_str) and rule2(next_str) and rule3(next_str):
            break
        else:
            string = next_str
    return next_str

puzzle_input = "vzbxkghb"
part1 = next_pw(puzzle_input)
part2 = next_pw(part1)
print(part2)


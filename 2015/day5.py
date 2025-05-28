from pathlib import Path
puzzle_input = Path(__file__).parent / 'inputday5.txt'

with open(puzzle_input, 'r') as archive:
    entries = [i.strip() for i in archive.readlines()]

'''
It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.'''


def part1():
    def is_nice(string):
        not_allowed = ['ab', 'cd', 'pq', 'xy']
        vowels = ('a', 'e', 'i', 'o', 'u')
        count_vowel = 0
        cur_letter = ""
        A, B, C = False, False, True
        for letter in string:
            dual = cur_letter + letter
            # print(dual)
                
            if letter == cur_letter:
                # print('B true')
                B = True
            if letter in vowels:
                count_vowel +=1
            if count_vowel == 3:
                # print('A true')
                A = True
            

            if dual in not_allowed:
                # print('C false')
                C = False

            
            cur_letter = letter

        if A and B and C:
            return True
        return False
    
    total = sum([1 for i in entries if is_nice(i)])
    print(total)


# part1()

#--- part 2 ---
'''
It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.'''
def is_nice2(string:str):
    # print()
    A, B = False, False
    duals = []

    for i in range(len(string)-1):
        dual = string[i] + string[i+1]
        try:
            if dual == string[i+2] + string[i+3]:
                A = True

        except:
            pass

        if dual in duals:

            if string[i] + string[i+1] != string[i-1] + string[i]:
                A = True

        
        try:
            if string[i] == string[i+2]:
                B = True

        except:
            pass

        duals.append(dual)

    if A and B:
        return True
    return False
        

total = 0 
for string in entries:
    if is_nice2(string):
        total +=1

print(total)


# print(is_nice2("bnbptgihhfubxhho"))

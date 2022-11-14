import time

"""
    
NOTES:

a)  
This was just a case of the fibonacci sequence whilst also converting the numbers to letters using the rules specified in the question

b)
This was just a brute force approach which worked quite well since the range of possibilities was quite low

c)
I guessed that there would be a loop since the values can't exceed 26, and after verifying this it turned out my guess was correct.
I then used this to figure out which part of the loop the very large number in the question would lie on.

"""

def getNthLetterInSeq(letter1, letter2, n):
    letter1 = ord(letter1) - 64
    letter2 = ord(letter2) - 64
    for i in range(3, n+1):
        nextLetter = letter1 + letter2
        while (nextLetter > 26):
            nextLetter -= 26
        letter1 = letter2
        letter2 = nextLetter
    if (n == 1): return chr(letter1 + 64)
    else: return chr(letter2 + 64)

def checkRepeatedItems(seq):
    return seq[len(seq)-2] == seq[0] and seq[len(seq)-1] == seq[1]
        

def part_a():
    with open("(1)-test.txt", "r") as f:
        content = f.readlines()
        for line in content:
            cin = line.split(" ")[:3]
            expected = line.split(" ")[-1].strip()
            cout = getNthLetterInSeq(cin[0], cin[1], int(cin[2]))
            status = "failed"
            if (cout == expected): status = "passed"
            print(f'status: {status} ||| input: {cin} ||| output: {cout} ||| expected: {expected}')
            
def part_b():
    numberF = ord("F") - 64
    sol1 = None
    for i in range(1, 27):
        offsetLetter = numberF + i
        while (offsetLetter > 26):
            offsetLetter -= 26
        if (chr(offsetLetter + 64) == "X"):
            sol1 = chr(i + 64)
            break
    
    numberQ = ord("Q") - 64
    sol2 = None
    for i in range(1, 27):
        offsetLetter = numberQ + i
        while (offsetLetter > 26):
            offsetLetter -= 26
        if (chr(offsetLetter + 64) == "H"):
            sol2 = chr(i + 64)
            break
    
    # sol1 is for the letter that combines with F to produce X and sol2 is the letter that combines with the letter Q to produce H. 
    print(sol1, sol2)

def part_c():
    seq = [3, 3, 6]
    n = 1_000_000_000_000_000_000
    while (checkRepeatedItems(seq) == False):
        nextLetter = seq[-1] + seq[-2]
        while (nextLetter > 26):
            nextLetter -= 26
        seq.append(nextLetter)
    seq.pop()
    seq.pop()
    print(chr(seq[n % len(seq)] + 64))
    

def main():
    startTime = time.time()
    
    # part_a()
    # part_b()
    # part_c()

    print(f'Execution time (seconds): {round(time.time() - startTime, 5)}')
    pass

if __name__ == "__main__":
    main()
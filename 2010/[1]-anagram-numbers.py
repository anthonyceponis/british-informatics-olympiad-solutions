import time
import math

"""
    
NOTES:

a)  
I implemented a fairly straight forward brute force algorithm. 
It did not use anything special other than making use of dictionaries to count occurences of digits.

b)
I could not be bothered to adjust the checkAnagram function to be able to solve both parts a and b so I just copy pasted certain parts that I need from it instead.

c)
I adjusted the checkAnagram function from part a to make it a bit faster (a.k.a pruning the search) by adding a fast setting.
This is becaues we were only interested in whether or not there existed at least one anagram that could be formed rather than how many there were or what they were.

"""

def checkAnagram(n, fastCheck = False):
    vaildMultipliers = []
    nTracker = {}
    for x in str(n):
        if (fastCheck and len(vaildMultipliers) > 0): break
        if x in nTracker:
            nTracker[x] += 1
        else:
            nTracker[x] = 1
    for i in range(2, 10):
        current = n * i
        currentTracker = {}
        for x in str(current):
            if x in currentTracker:
                currentTracker[x] += 1
            else:
                currentTracker[x] = 1
        if (len(currentTracker.keys()) != len(nTracker.keys())): continue
        valid = True
        for x in currentTracker.keys():
            if x not in nTracker or nTracker[x] != currentTracker[x]: 
                valid = False
                break
        if valid:
            vaildMultipliers.append(i)
    return vaildMultipliers
            
            

def part_a():
    with open("(1)-test.txt", "r") as f:
        content = f.readlines()
        for line in content:
            cin = int(line.split(" ")[0])
            expected = "".join(f'{x.strip()} ' for x in line.split(" ")[1:])
            cout = checkAnagram(cin)
            if (len(cout) == 0): cout = "NO "
            else: cout = "".join(f'{x} ' for x in cout)
            status = "failed"
            if (cout == expected): status = "passed"
            print(f'status: {status} ||| input: {cin} ||| output: {cout} ||| expected: {expected}')
            
def part_b():
    n = 85247910
    nTracker = {}
    for x in str(n):
        if x in nTracker:
            nTracker[x] += 1
        else:
            nTracker[x] = 1
    anagrams = []
    for i in range(2, 10):
        current = n / i
        if math.floor(current) != current: continue
        current = int(current)
        currentTracker = {}
        for x in str(current):
            if x in currentTracker:
                currentTracker[x] += 1
            else:
                currentTracker[x] = 1
        if (len(currentTracker.keys()) != len(nTracker.keys())): continue
        valid = True
        for x in currentTracker.keys():
            if x not in nTracker or nTracker[x] != currentTracker[x]: 
                valid = False
                break
        if valid:
            anagrams.append(current)
    print(anagrams)
    
def part_c():
    num = 0
    for i in range(100_000, 1_000_000):
        removeDuplicates = set()
        for x in str(i):
            removeDuplicates.add(x)
        if len(removeDuplicates) != len(str(i)): continue
        if (len(checkAnagram(i, True)) > 0):
            num += 1
    print(num)
        

def main():
    startTime = time.time()
    
    # part_a()
    # part_b()
    # part_c()

    print(f'Execution time (seconds): {round(time.time() - startTime, 5)}')
    pass

if __name__ == "__main__":
    main()
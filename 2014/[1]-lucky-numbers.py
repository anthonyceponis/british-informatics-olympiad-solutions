import time

"""
    
NOTES:

a)  
For this problem, I used a similar idea to the seive of eratosthenes where I filtered out numbers as we go along.
I guessed that consecutive lucky numbers will be within 1000 numbers apart to find the upper bound.
I doubt this is the best/most efficient solution but it is fast enough for the competition.

b)
I just reused the algorithm for getting the closest lucky numbers for all numbers between 1 and 100 and removed duplicates

"""

def getClosestLuckyNumbers(cin):
    nums = []
    luckyNums = [1]
    i = 1
    while (2*i-1 <= cin + 1000):
        nums.append(2*i-1)
        i+=1
    
    for i in nums:
        if (i <= 1): continue
        position = 1
        for j in range(len(nums)):
            if (nums[j] < 0): continue
            if (position % i == 0): nums[j] = -1
            position += 1
        luckyNums.append(i)
    
    moreThanClosest = None
    lessThanClosest = None
    for i in range(len(luckyNums)):
        if (luckyNums[i] > cin): 
            moreThanClosest = luckyNums[i]
            if (luckyNums[i-1] == cin): lessThanClosest = luckyNums[i-2]
            else: lessThanClosest = luckyNums[i-1]
            break
    
    return [lessThanClosest, moreThanClosest]

def part_a():
    with open("(1)-test.txt", "r") as f:
        content = f.readlines()
        for line in content:
            cin = int(line.split(" ")[0].strip())
            expected = " ".join(line.split(" ")[1:]).strip()
            cout = " ".join(f'{x}' for x in getClosestLuckyNumbers(cin))
            status = "failed"
            if (cout == expected): status = "passed"
            print(f'status: {status} ||| input: {cin} ||| output: {cout} ||| expected: {expected}')
            
            
def part_b():
    luckyNums = {1}
    for i in range(2, 101):
        luckyNums.add(getClosestLuckyNumbers(i)[0])
    print(len(luckyNums))

def part_c():
    """ 
    
    I did some trial and error on paper with small cases and saw that the nth lucky number will have 2*n - 2 outputs.
    So applying the formula to n = 1,000,000,000 we get 1,999,999,998 different results.
    
    """
    

def main():
    startTime = time.time()
    
    # part_a()
    # part_b()
    # part_c()

    print(f'Execution time (seconds): {round(time.time() - startTime, 5)}')
    pass

if __name__ == "__main__":
    main()
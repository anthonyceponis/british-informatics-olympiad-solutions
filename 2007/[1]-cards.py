import time
import itertools
import math

"""
    
NOTES:

a)  
It was easier to split this into checking the two different ways of gaining points.
I used the binomial function from the math module to see how many ways I can choose two cards from any number of repeats.
For the second part, I just created all possible subsets and filtered those that sum to 15.

c)
I was constantly getting an answer of 29 and was incredibly confused as to why it was incorrect. 
Then I saw that you can only use the same card at a maximum of 4 times, clearly written in bold text lol.
I guess it is a reminder for me to always read the question carefully, off by 1 errors are silly way to not gain credit. 
However, the mark scheme still gave you 3 out of the 4 marks available if you gave an answer of 29.  
I could have wasted time making an algorithm that checks if a card has more than 4 of the same card, but it was quicker to just print them out and check by hand.
In this case, it was only the 3,3,3,3,3 case. 
My method ensured to not generate duplicate sets by ensuring that the items in each set were constructed in non-decreasing order.

"""

def getPoints(nums):
    ways = 0
    
    # First we count the number of identical pairs
    itemTracker = {}
    for i in nums:
        if i in itemTracker.keys():
            itemTracker[i] += 1
        else:
            itemTracker[i] = 1
    for i in itemTracker.keys():
        if (itemTracker[i] >= 2):
            ways += math.comb(itemTracker[i], 2)
    
    # Now we count the number of ways to form 15
    for x in range(1, len(nums) + 1):
        subsets = list(itertools.combinations(nums, x))
        for i in subsets:
            localSum = 0
            for j in i:
                localSum += j
                if localSum > 15: break
            if localSum == 15: ways += 1
        
    return ways   

def part_a():
    with open("(1)-test.txt", "r") as f:
        content = f.readlines()
        for line in content:
            cin = [int(x) for x in line.split(" ")[:5]]
            expected = int(line.split(" ")[-1].strip())
            cout = getPoints(cin)
            status = "failed"
            if (cout == expected): status = "passed"
            print(f'status: {status} ||| input: {cin} ||| output: {cout} ||| expected: {expected}')    
            
def part_b():
    """
    
    It is quite easy to come up with an example that does not satisfy the first condition (of not containing duplicates).
    The second condition can be easily satisfied by using the fact that 15 is odd. 
    So, if we use the first 5 even numbers, we are guaranteed to have an even sum no matter which subset we create, which guarantees that we will never get a sum of 15.
    So a set that works is 2,4,6,8,10.
    
    """
    
def part_c():
    examples = []
    for a in range(1, 11):
        for b in range(a, 11):
            for c in range(b, 11):
                for d in range(c, 11):
                    for e in range(d, 11):
                        if a + b + c + d + e == 15:
                            examples.append([a, b, c, d, e])
    examples.pop()
    print(len(examples))

def main():
    startTime = time.time()
    
    # part_a()
    # part_b()
    # part_c()

    print(f'Execution time (seconds): {round(time.time() - startTime, 5)}')
    pass

if __name__ == "__main__":
    main()
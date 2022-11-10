import math
import time

"""

NOTES:

a)
Split into the cases of even and odd length. 
Use this to get the first half of the number.
Reverse the first half and then add the first half of the number to the reverse of the first half to construct a palindrome.
In some cases, the constructed palindrome will be less than the input number, so we get the first half and numerically increment by 1 and repeat the process above.

b)
I just experimented with different strings of length 20 that could potentially be the answer (given that brute forcing was not really an option that worked for me).
After coding part a, I saw how the middle numbers often had the largest impact which then quickly lead me to a convincing solution.

c) - SLOW
A straight forward brute force approach that checks all possible numbers that can be written as a sum of two palindromes and then subtracting to find those that can't.

"""

def nextPalindrome(num, depth = 0):
    next = num
    
    if (len(num) % 2 == 0):
        half = num[0:int(len(num) / 2)]
        next = half + half[::-1]
    elif (len(num) % 2 == 1):
        half = num[0:int((len(num)-1) / 2)]
        next = half + num[int((len(num) - 1)/2)] + half[::-1]
    
    if (int(next) <= int(num) and depth == 0):
        pwr = int(math.floor(len(next) / 2))
        next = (math.floor((int(next) / pow(10, pwr))) + 1) * pow(10, pwr);
        return nextPalindrome(str(next), 1)
        
    return next

def part_a():
    with open("(1)-test.txt", "r") as f:
        content = f.readlines()
        for line in content:
            num = line.split(" ")[0].strip()
            expected = line.split(" ")[1].strip()
            next = nextPalindrome(num)
            successString = "Failed"
            if (next == expected): successString = "Passed"
            print(f'Status: {successString} ||| Input: {num} ||| Output: {next} ||| Expected: {expected}')

            
def part_b():
    print(f'{int(nextPalindrome("99999999911999999999")) -  99_999_999_911_999_999_999:,}')

def part_c():
    n1 = 0
    nums = set()
    while (n1 <= 99_999):
        n2 = 1;
        while (n2 <= 99_999):
            if (1 <= n1+n2 <= 99_999):
                nums.add(n1+n2)
                n2 = int(nextPalindrome(str(n2)))
            else: break;
        n1 = int(nextPalindrome(str(n1)))
    print(99_999 - len(nums))
    
            
    
def main():
    startTime = time.time()
    
    # part_a()
    # part_b()
    # part_c()
    
    print(f'Execution time (seconds): {round(time.time() - startTime, 5)}')
    pass
    

if __name__ == "__main__":
    main()
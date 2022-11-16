import time

"""
    
NOTES:

a)  
This is another systematic brute force approach that first creates a sieve of erastosthenes and then checks all possible cases.
I only checked half of the possible sums to avoid double counting sums (as all sums can be flipped when they are infact the same sum e.g. a + b = b + a).

b)
I updated the function from part a to actually track the sums that are being checked and return them if needed. 

c)
I agree this is not the best way to do it because you could probably use the fact that 2 is the only even prime and so even + odd = odd.
But since the given domain was quite small, I just did the first implementation that came to mind which is still plenty fast.

"""

def sieveOfEratosthenes(n):
    sieve = [True] * (n+1)
    sieve[0] = False
    sieve[1] = False
    finalSieve = []
    for i in range(2, n):
        counter = 2
        if (sieve[i]): finalSieve.append(i)
        while (counter * i <= n):
            sieve[counter * i] = False
            counter += 1
    return finalSieve

def getPrimeSumWays(n, includeWays = False):
    sieve = sieveOfEratosthenes(n)
    i = 0
    ways = 0
    examples = []
    while sieve[i] <= int(n/2):
        if n - sieve[i] in sieve: 
            ways += 1
            examples.append([sieve[i], n-sieve[i]])
        i += 1
    if includeWays == True: return examples
    return ways


def part_a():
    with open("(1)-test.txt", "r") as f:
        content = f.readlines()
        for line in content:
            cin = int(line.split(" ")[0])
            expected = int(line.split(" ")[1].strip())
            cout = getPrimeSumWays(cin)
            status = "failed"
            if (cout == expected): status = "passed"
            print(f'status: {status} ||| input: {cin} ||| output: {cout} ||| expected: {expected}')

def part_b():
    ways = getPrimeSumWays(46, True)
    for i in ways:
        print(f'{i[0]} + {i[1]}')

def part_c():
    nums = 0
    for i in range(4, 51):
        if (i % 2 == 0): continue
        if (getPrimeSumWays(i) == 0): nums += 1
    print(nums)

def main():
    startTime = time.time()
    
    # part_a()
    # part_b()
    # part_c()

    print(f'Execution time (seconds): {round(time.time() - startTime, 5)}')
    pass

if __name__ == "__main__":
    main()
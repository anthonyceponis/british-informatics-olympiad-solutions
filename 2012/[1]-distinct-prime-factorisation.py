import time

"""
    
NOTES:

a)  
The crux of this problem was just knowing how to use the sieve of erastosthenes to generate primes.
Checking the product was then a simple loop through the sieve.
I optimised my solution for checking many cases which is why I done the sieve first and then checked the products. 
In the competition, it would be better to optimise for a cases by case basis and therefore only generate as large of a sieve as you need for each case.

c)
I am not quite sure how to do this without brute force. 
It is something to do with consecutive primes because the answer is 210 = 2 x 3 x 5 x 7 but I am not sure how to prove this.

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

def getDistinctProduct(n, sieve):
    product = 1
    for i in sieve:
        if (i > n): break
        if (n % i == 0): product *= i
    return product

def part_a():
    sieve = sieveOfEratosthenes(1_000_000)
    print(getDistinctProduct(101, sieve))
    with open("(1)-test.txt", "r") as f:
        content = f.readlines()
        for line in content:
            cin = int(line.split(" ")[0].strip())
            expected = int(line.split(" ")[1].strip())
            cout = getDistinctProduct(cin, sieve)
            status = "failed"
            if (cout == expected): status = "passed"
            print(f'status: {status} ||| input: {cin} ||| output: {cout} ||| expected: {expected}')
            
def part_b():
    """ 
    
    2 x 2 < 5 and 2 x 2 x 2 > 5 are two useful facts for finding the minimal cases.
    We can construct our cases working our way up using these two facts. It must include a 2 x 5 so lets just consider the 'extra' 2's and 5's.
    1
    2
    2 x 2 = 4
    5 = 5
    2 x 2 x 2 = 8
    2 x 5 = 10
    2 x 2 x 2 x 2 = 16
    2 x 5 x 2 = 20
    5 x 5 = 25
    2 x 2 x 2 x 2 x 2 = 32
    
    So our numbers will be the above times 10 which are: 10, 20, 40, 50, 80, 100, 160, 200, 250, 320.
    
    """

def part_c():
    sieve = sieveOfEratosthenes(1_000_000)
    products = {}
    mostFrequentProduct = None
    frequency = 1
    for i in range(1, 1_000_000):
        print(i)
        product = getDistinctProduct(i, sieve)
        if (product in products): products[product] += 1
        else: products[product] = 1
    
    for i in products.keys():
        if (products[i] > frequency): 
            frequency = products[i]
            mostFrequentProduct = i
    print(mostFrequentProduct)

def main():
    startTime = time.time()
    
    # part_a()
    # part_b()
    # part_c()

    print(f'Execution time (seconds): {round(time.time() - startTime, 5)}')
    pass

if __name__ == "__main__":
    main()
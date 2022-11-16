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
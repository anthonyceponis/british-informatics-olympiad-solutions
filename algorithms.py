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

# Check if str2 is a rotation of str1
def isRotation(str1, str2):
    if len(str1) != len(str2): return False
    
    startingIndexes = []
    for i in range(len(str1)):
        if str1[0] == str2[i]:
            startingIndexes.append(i)
    
    if len(startingIndexes) == 0: return False
    
    rotation = False
    
    for i in startingIndexes:
        rotation = True
        for j in range(len(str1)):
            if str1[j] != str2[(j + i) % len(str1)]: 
                rotation = False
                break
    
    return rotation
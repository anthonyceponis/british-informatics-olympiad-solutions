import time

""" 

NOTES:

a)
I just generated all partitions of the string and then checked those that are satisfied with the block palindrome condition. 
This might not be the most efficient way but it is fast enough for the inputs given.

"""

def isPalindrome(str):
    return str == reversed(str)

def getPartitions(string, index, out, ways):
    if index == len(string):
        ways.append(out)
 
    for i in range(index, len(string)):
        newOut = out[:]
        newOut.append(string[index:i + 1])
        getPartitions(string, i + 1, newOut, ways)
        
def arraysEqual(arr1, arr2, printArr = False):
    if (len(arr1) != len(arr2)): return False
    for i in range(len(arr1)):
        if (arr1[i] != arr2[i]): return False
    if (len(arr1) > 1 and printArr): print("".join(f'({w})' for w in arr1))
    return True

def getNumberOfBlockPalindromes(cin, printWays = False):
    blockPalindromes = 0
    ways = []
    out = []
    getPartitions(cin, 0, out, ways)
    for way in ways: 
        if (arraysEqual(way, list(reversed(way)), printWays)): blockPalindromes += 1
    
    # Must subtract 1 because of the case where the entire string is considered as a single block
    return blockPalindromes - 1
        

def part_a():
    with open("(1)-test.txt", "r") as f:
        content = f.readlines()
        for line in content:
            cin = line.split(" ")[0].strip()
            expected = int(line.split(" ")[1].strip())
            cout = getNumberOfBlockPalindromes(cin)
            status = "failed"
            if (cout == expected): status = "passed"
            print(f'status: {status} ||| input: {cin} ||| output: {cout} ||| expected: {expected}')
      
def part_b():  
    getNumberOfBlockPalindromes("AABCBAA", True)
    
def part_c():
    """ 
    
    Must have an even ammount of letters.
    This is because the first half of the blocks is equal to the last and there is an even number of blocks which means the entire length must be divisible by 2.
    There must be only 1 grouping because if a grouping does contain more than 2 blocks then combining the middle blocks would still be valid but would make an odd number of blocks which is a contradiction.
    
    """

def main():
    startTime = time.time()
    
    # part_a()
    # part_b()
   
    print(f'Execution time (seconds): {round(time.time() - startTime, 5)}')
    pass

if __name__ == "__main__":
    main()
import time

"""
    
NOTES:

a)  
This was a fairly straight forward brute force approach which checks the every character is found in every digit word

"""

def getDigitWord(word):
    words = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    for i in range(len(words)):
        currentComparisonWordIndex = 0
        for j in range(len(word)):
            if words[i][currentComparisonWordIndex] == word[j]:
                currentComparisonWordIndex += 1
            if currentComparisonWordIndex == len(words[i]):
                return str(i+1)
    return "NO"
    
            

def part_a():
    with open("(1)-test.txt", "r") as f:
        content = f.readlines()
        for line in content:
            cin = line.split(" ")[0].strip()
            expected = line.split(" ")[1].strip()
            cout = getDigitWord(cin)
            status = "failed"
            if (cout == expected): status = "passed"
            print(f'status: {status} ||| input: {cin} ||| output: {cout} ||| expected: {expected}')

def part_b():
    """
    
    We must choose 1 T, 1 W and 1 O. 
    If we choose the last T, there is only one way.
    If we choose the middle T, we can choose the middle W and then either of the O's or we can choose the last W and the last O. Therefore, there are 2 + 1 = 3 ways.
    If we choose the first T, we can either choose the last W and the last O, the middle W and either of the two last O's or the first O and any of the O's. Therefore there are 1 + 2 + 3 = 6 ways.
    Therefore, in all cases we have a total of 1 + 3 + 6 = 10 ways.
    
    """
    
def part_c():
    """
    
    We can construct a smallest length word containing the digits ONE to FIVE by writing out all the numbers (as words) and placing certain letters in order and working systematically.
    A shortest length word will the the length of all distinct letters that appear the most number of times in a particular word.
    For example, using the digit words ONE and THREE, E is used twice in THREE so we use two E's rather than 1 etc.
    So, the shortest length word that contains the digits 1 to 5 is of length 12 and one example of such word is TWFONHURIVEE.
    The shortest length word that contains the digits 1 to 10 cannot be constructed using the same rules as before since there are edge cases where letters must appear before and after certain letters, like in the numbers EIGHT and THREE.
    After some careful construction, an example I came up with was SFEVIXGHTWHOURVENE which is of minimal length 18.
    
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
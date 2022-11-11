import time

"""
    
NOTES:

a)
Simply translates the steps of the algorithm into code.    

"""

def getPromenadeOutput(cin):
    beforeMostRecentLeftChoice = [1, 0]
    beforeMostRecentRightChoice = [0, 1]
    mostRecent = [1, 1]
    
    for letter in cin:
        if (letter == "L"):
            beforeMostRecentLeftChoice = mostRecent[:]
        elif (letter == "R"):
            beforeMostRecentRightChoice = mostRecent[:]
        
        l = beforeMostRecentLeftChoice[0]
        m = beforeMostRecentLeftChoice[1]
        r = beforeMostRecentRightChoice[0]
        s = beforeMostRecentRightChoice[1]
        
        mostRecent[0] = l+r
        mostRecent[1] = m+s
    
    return f'{mostRecent[0]}/{mostRecent[1]}'

def part_a():
    with open("(1)-test.txt", "r") as f:
        content = f.readlines()
        for line in content:
            cin = line.split(" ")[0].strip()
            expected = "".join(line.split(" ")[1:]).strip()
            cout = getPromenadeOutput(cin)
            status = "failed"
            if (cout == expected): status = "passed"
            print(f'status: {status} ||| input: {cin} ||| output: {cout} ||| expected: {expected}')

def part_b():
    """
    
    I just checked what LRL + LLLL is numerically which is 4/5.
    I then just did some guestimating and found that LRRR was the solution.
    
    """

def part_c():
    """
    
    After some playing around, I found that a string of n L's leads to a fraction of 1/(n+1).
    Therefore, 1/1,000,000 can be represented as a promenade of 999,999 L's (and 0 R's).
    
    """

def part_d():
    """
    
    The promenade conversion algorithm does not contain any minus signs and the null promenade is positive which means it is impossible to represent a negative fraction.
    
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
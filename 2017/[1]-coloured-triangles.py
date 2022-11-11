import time

"""
    
NOTES:

a)
This is just a simple for loop that checks adjacent squares and appends the output square to the next row based on the restrictions given in the question.
    
"""

def getOpposite(col1, col2):
    cols = [col1, col2]
    r_found = False
    g_found = False
    b_found = False
    
    for i in cols:
        if (i == "R"): r_found = True
        elif (i == "G"): g_found = True
        elif (i == "B"): b_found = True

    if (r_found == False): return "R"
    elif (g_found == False): return "G"
    elif (b_found == False): return "B"
    
def getFinalLetter(firstRow):
    row1 = firstRow
    row2 = ""
    while (len(row1) >=2):
        for i in range(len(row1)-1):
            if (row1[i] == row1[i+1]): row2 += row1[i]
            else: row2 += getOpposite(row1[i], row1[i+1])
        row1 = row2
        row2 = ""
    return row1

def part_a():
    with open("(1)-test.txt", "r") as f:
        content = f.readlines()
        for line in content:
            cin = line.split(" ")[0].strip()
            expected = line.split(" ")[1].strip()
            cout = getFinalLetter(cin)
            status = "failed"
            if (cout == expected): status = "passed"
            print(f'status: {status} ||| input: {cin} ||| output: {cout} ||| expected: {expected}')
                
def part_b():
    """ 
    
    Case first letter R:
       R R R B B G G R G
        R R G B R G B B
    
        This is the only possible way as the first letter locks the rest of the letters due to the restrictions in the question.
    
    Case first letter is G:
       G B G G R R B B B
        R R G B R G B B
        
    Case first letter B:
       B G B R G B R G R 
        R R G B R G B B
        
        First letter locks the rest again.
    
        
    So the only possible cases are RRRBBGGRG, GBGGRRBBB, BGBRGBRGR.
    
    """
            
def part_c():
    
    """
    
    Experimenting:
    Suppose you have the following triangle:    _ R _ _
                                                 _ B _
                                                  R _
                                                   R  
                                                   
    Working from the bottom up, there is only one way to complete the second to bottom row clearly. 
    Then, working up there will be only one way to fill the right most space on the second row and one way to fill the left most space which completes the row.
    A similar arguement follows for the first row.
    So it seems reasonable that there is only one way to complete the triangle.
                         
    Inductive justification:
    Consider the kth row (from the bottom) that is completely filled. 
    The letters on either side of the letter on the (k+1)th row that is filled by default can only be filled in one way. 
    Using this idea, the rest of the row can be filled uniquely.
    Now I have shown that if a row is filled then we can fill the row above, but the row at the bottom is filled by default so we can fill the entire triangle in only one way.
    
    """ 

def part_d():
    """
    
    Let R = 0, G = 1, B = 2
    
    The only possible sums are R+G+B, R+R+R, G+G+G, B+B+B which equal 3, 0, 3, 6 respectively, which are all divisble by 3.
    
    Consider the top squares and label them from left to right as a1, a2, a3, a4, ..., an.
    Consider the effect of each square from the first row on the final row, i.e. count how many times the square ai for 1 <= i <= n is counted in the final row.
    The sum of the effect of all squares will be the same mod 3. To ensure that only the extreme sides of the first row are the only squares that effect the outcome,
    we must ensure that the sum of the effect of all other squares are divisible by 3. 
    
    Example for n = 4 consider i = 2:
    
        At the start, the effect of a2 = 1
    
        _ 1 _ _
         1 1 _
          1 1
           2
           
        This can be translated to traversing a grid of size i x (n-r-1) and there are (n-1) CHOOSE i ways (choose function) to traverse this grid which is the effect of ai on the final element.
        Now, we must ensure that the sum of (n-1) CHOOSE i for 2 <= i <= n-1 is divisible by 3. 
        Using the hockey stick identity, we have that this sum is equal to (n-1+1) CHOOSE 3 which is equal to n CHOOSE 3. 
        We need the smallest n greater than 4 such that n CHOOSE 3 is divisible by 3.
        After some trial and error you will find that the smallest case is n = 10.
    
    """

def main():
    startTime = time.time()
    
    # part_a()
    # part_b()
    # part_c()
    # part_d()

    print(f'Execution time (seconds): {round(time.time() - startTime, 5)}')
    pass

if __name__ == "__main__":
    main()
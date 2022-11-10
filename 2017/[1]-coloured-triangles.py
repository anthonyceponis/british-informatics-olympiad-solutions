import time

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
    
    pass   
            
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
    
    pass

def part_d():
    """
    
    Cases for extreme left and right are the following: RR, BB, GG, RB, BR, RG, GR, BG, GB
    
    """
    
    pass

def main():
    startTime = time.time()
    
    part_a()
    # part_b()
    # part_c()
    # part_d()
    

    print(f'Execution time (seconds): {round(time.time() - startTime, 5)}')
    pass

if __name__ == "__main__":
    main()
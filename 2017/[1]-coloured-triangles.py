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
    # For manual input
    # firstRow = input()
    
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
    
        This is the only possible way as the first letter locks the rest of the letters due to the restrictions in the question
    
    Case first letter B:
       B G B R G B R G R 
        R R G B R G B B
        
        First letter locks the rest again
    
    Case first letter is G:
       G B G G R R B B B
        R R G B R G B B
        
    So the only possible cases are RRRBBGGRG, BGBRGBRGR, GBGGRRBBB
    
    """
    
    pass   
            

def main():
    startTime = time.time()
    
   
    part_a()
    

    print(f'Execution time (seconds): {round(time.time() - startTime, 5)}')
    pass

if __name__ == "__main__":
    main()
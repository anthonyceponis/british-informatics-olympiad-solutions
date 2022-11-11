import time

def getNumberOfBlockPalindromes():
    pass

def part_a():
    with open("(1)-test.txt", "r") as f:
        content = f.readlines()
        for line in content:
            cin = line.split(" ")[0].strip()
            expected = line.split(" ")[1].strip()
            cout = None
            status = "failed"
            if (cout == expected): status = "passed"
            print(f'status: {status} ||| input: {cin} ||| output: {cout} ||| expected: {expected}')
    
    ################################################################################################################
    # START HERE
    ################################################################################################################
    
    
    
    
    
    pass

def main():
    startTime = time.time()
    
    

    print(f'Execution time (seconds): {round(time.time() - startTime, 5)}')
    pass

if __name__ == "__main__":
    main()
import time

"""
    
NOTES:

a)
This is essentially just programming tetris but without all of the UI razzle dazzle. 
I made use of 'bubble-like' sorting to simplify the grid, a 'dfs-like' algorithm to find blocks and kind of like a conveyor belt system to refill blocks where I used pointers rather than actually moving cells in the refill grid.

"""

# Conveyor belt system needs to be implemented
def restockGrid(currentGrid, refillGrid, restockIndexes):
    for col in range(4):
        for row in range(3, -1, -1):
            if currentGrid[row][col] == None:
                currentGrid[row][col] = refillGrid[restockIndexes[col]][col]
                restockIndexes[col] -= 1
                if restockIndexes[col] < 0: restockIndexes[col] = 3

def simplifyGrid(currentGrid):
    for col in range(4):
        swapsMade = True
        while swapsMade:
            swapsMade = False
            row = None
            for i in range(2, -1, -1):
                if currentGrid[i][col] != None and currentGrid[i+1][col] == None:
                    row = i
                    break
            # If row is none it means that there is nothing left to swap/simplify
            while row != None and row <= 2 and currentGrid[row+1][col] == None:
                currentGrid[row+1][col], currentGrid[row][col] = currentGrid[row][col], currentGrid[row+1][col]
                swapsMade = True
                row += 1
             
def removeBlocksAndGetScore(currentGrid, visitedTracker):
    scores = []
    counterPtr = [0]
    for y in range(4):
        for x in range(4):
            counterPtr[0] = 0
            explore(currentGrid, visitedTracker, x, y, counterPtr, currentGrid[y][x])
            scores.append(max(1,counterPtr[0]))
    score = 1
    for i in scores:
        score *= i
    if score == 1: score = 0
    return score

def explore(currentGrid, visitedTracker, x, y, counterPtr, letter):
    if visitedTracker[y][x] == True or currentGrid[y][x] != letter or currentGrid[y][x] == None:
        return
    counterPtr[0] += 1
    visitedTracker[y][x] = True
    if x > 0:
        explore(currentGrid, visitedTracker, x-1, y, counterPtr, letter)
    if x < 3:
        explore(currentGrid, visitedTracker, x+1, y, counterPtr, letter)
    if y < 3:
        explore(currentGrid, visitedTracker, x, y+1, counterPtr, letter)
    if counterPtr[0] >= 2:
        currentGrid[y][x] = None
    return

def printFormattedGrid(currentGrid):
    for i in currentGrid:
        print("".join(i))
            
def playRound(currentGrid, refillGrid, restockIndexes, visitedTracker):
    score = removeBlocksAndGetScore(currentGrid, visitedTracker)
    simplifyGrid(currentGrid)
    restockGrid(currentGrid, refillGrid, restockIndexes)
    printFormattedGrid(currentGrid)
    return score

def part_a():
    refillGrid = []
    restockIndexes = [3, 3, 3, 3]
    currentGrid = []
    visitedTracker = [[False]*4 for i in range(4)]
    score = 0
    for i in range(4):
        cin = list(input())
        currentGrid.append(cin[:])
        refillGrid.append(cin[:])
        
    n = 1
    
    while n > 0:
        n = int(input())
        for i in range(n):
            prevScore = score
            score += playRound(currentGrid, refillGrid, restockIndexes, visitedTracker)
            visitedTracker = [[False]*4 for i in range(4)]
            print(score)
            if score == prevScore:
                print("GAME OVER")
                n = 0
                break        

def part_b():
    """
    
    The prime factorisation of 105 = 3 * 5 * 7
    Clearly, if we combine any of the factors to create a larger block then it won't work. 
    So we must have 3 independent blocks of sizes 3, 5 and 7. 
    This creates 3 + 5 + 7 = 15 cells so we will have 1 extra since we require 16 cells for a grid.
    We must be careful to place the final cell in a place that does not connect to an existing block.
    
    An example configuration is the following: RRRG
                                               GGGG
                                               BBBB
                                               BBBR
    
    """
    
def part_c():
    """
    
    Not quite sure how to justify as to 'why' this is the maximum.
    However, my thinking was that I need to maximise the size of the blocks whilst also maximising the frequency of blocks.
    I started with powers of 2 and 2^8 = 256. Similarly I found it using blocks of size 4 which was 4^4 = 2^8 = 256.
    So I went in between and found 4 blocks of size 3 and a final block of size 4 which yielded 3^4 * 4 = 324 which is the maximum.
    
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
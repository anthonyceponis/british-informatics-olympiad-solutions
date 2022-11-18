import time
import itertools

"""
    
NOTES:

a)  
Since this was an implementation question, I have instead annotated my solution with many comments.
I have avoided using the official terminology of the question, such as kawai and putahi, since it can be confusing and non-descriptive.
My main approach was creating a function that checks if a player is in a winning position and another function that checks which move to play next.
For the function that checks which move to play next, I added a forward check parameter to prevent infinite recursion in the cases where we check for a defensive move.

P.S.
This is my first q2 I have solved so don't expect this to be the most amazing solution.

"""

# player can be either "O" (player 1) or "X" (player 2)
# We check if that player is in a winning position if the opponent can no longer make a move
def isWinningPosition(player, state):
    opponent = "X"
    empty = "E"
    if player == "X": opponent = "O"
    middle = state[0]  
    
    # If the opponent is in the middle then he can always freely move out to the circumference
    if middle == opponent: return False  
    
    for i in range (1, len(state)):
        if (state[i] == opponent):
            left = i-1
            right = i+1
            # Must correct positions in the case of an overflow
            if left == 0: left = len(state)-1
            if right == len(state): right = 1
            
            # If either side is empty, then the opponent can still move
            if state[left] == empty or state[right] == empty: return False
            
            # If at least one of the left or right cells is not the opponent cells and the middle is empty, the opponent can still move into the middle
            if middle == empty and (state[left] != opponent or state[right] != opponent): return False
    return True

# player in this case is the player that is about to make a move
# It will return in the format [state, TRUE/FALSE] 
# TRUE means that the player has won 
# FALSE means that the player has lost in the current step
# NONE means that the player has not made a move to win in the current step 
def checkMovesAndGetNextBoardState(player, state, forwardCheck = False):
    middle = state[0]
    empty = "E"
    opponent = "X"
    
    # In the case that we are already in a loosing position
    if isWinningPosition(opponent, state):
        return [state, False]
    
    if player == "X": opponent = "O"
    emptyIndex = None
    for i in range(len(state)):
        if state[i] == empty:
            emptyIndex = i
            break
    
    # There must be a default state in the case that the player cannot move into the winning position 
    defaultState = None
    
    # This is the state that gets entered if it is not possible for the player to win after making 1 move
    nonLoosingState = None
    
    # Must check the case involving the middle cell
    if middle == player:
        tempState = state[:]
        tempState[0] = empty
        tempState[emptyIndex] = player
        if defaultState == None:
            defaultState = tempState[:]
        if isWinningPosition(player, tempState[:]):
            return [tempState, True]
        if not forwardCheck and nonLoosingState == None and checkMovesAndGetNextBoardState(opponent, tempState[:], True)[1] != True:
            nonLoosingState = tempState[:]            
    
    # Checking the cases of the outer cells
    for i in range(1, len(state)):
        # We only need to inspect states of the current player rather than the opponent or the empty cell
        if state[i] != player: continue
        
        left = i-1
        right = i+1
        # Must correct positions in the case of an overflow
        if left == 0: left = len(state)-1
        if right == len(state): right = 1
        
         # Check a swap with the middle
        if middle == empty and (state[left] != player or state[right] != player):
            tempState = state[:]
            tempState[i] = empty
            tempState[0] = player
            if defaultState == None: 
                defaultState = tempState[:]
            if isWinningPosition(player, tempState[:]):
                return [tempState, True]
            if not forwardCheck and nonLoosingState == None and checkMovesAndGetNextBoardState(opponent, tempState[:], True)[1] != True:
                nonLoosingState = tempState[:]
        
        # Check the left and right swaps
        if state[left] == empty:
            tempState = state[:]
            tempState[i] = empty
            tempState[left] = player
            if defaultState == None: 
                defaultState = tempState[:]
            if isWinningPosition(player, tempState[:]):
                return [tempState, True]
            if not forwardCheck and nonLoosingState == None and checkMovesAndGetNextBoardState(opponent, tempState[:], True)[1] != True:
                nonLoosingState = tempState[:]
        
        if state[right] == empty:
            tempState = state[:]
            tempState[i] = empty
            tempState[right] = player
            if defaultState == None: 
                defaultState = tempState[:]
            if isWinningPosition(player, tempState[:]):
                return [tempState, True]
            if not forwardCheck and nonLoosingState == None and checkMovesAndGetNextBoardState(opponent, tempState[:], True)[1] != True:
                nonLoosingState = tempState[:]
    
    if nonLoosingState == None:
        return [defaultState, None]
    return [nonLoosingState, None]

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

def getInput():
    cin = input("Mode: ")
    while cin != "n" and cin != "r":
        print("Please enter 'n' or 'r' only")
        cin = input("Mode: ")
    return cin

def part_a():
    state = input("State: ").strip()
    
    # This is either n or r
    mode = getInput()
    
    player = "O"
    stateHistory = set()
    out = None
    
    
    while True:
        # Returns in the form [state, TRUE/FALSE/NONE]
        result = checkMovesAndGetNextBoardState(player, list(state))
        state = "".join(result[0])
        if mode == "n": 
            print()
            print(state)
        if result[1] == True:
            if player == "O": out = "Player 1 wins"
            elif player == "X": out = "Player 2 wins"
            stateHistory.add(state)
            break
        if result[1] == False:
            if player == "O": out = "Player 2 wins"
            elif player == "X": out = "Player 1 wins"
            stateHistory.add(state)
            break
        elif state in stateHistory:
            out = "Draw"
            break
        
        stateHistory.add(state)
        
        if player == "O": player = "X"
        elif player == "X": player = "O"
        
        if mode != "r":
            mode = getInput()
    
    if mode == "r":
        print()
        print(state)
    print(out)
    
def part_b():
    """
    
    The possible moves are XOOXXXOOE and XOEXXXOOO which can be deduced after drawing a diagram on paper.
    The move that will be played using the simple strategy will be XOOXXXOOE (the first move from above), which I checked using my function below.
    
    """
    print("".join(checkMovesAndGetNextBoardState("O", list("XEOXXXOOO"))[0]))
    
def part_c():
    """
    
    It can be split into two cases: 
    
    1. If there is a marker in the central position then they can always move out and so no player will be trapped into loosing.
    2. If there is no marker in the central position, there will always be a marker that has markers of opposing players either side and so will always be able to move into the middle.
       This is true because there are an equal ammount of markers from each team.
    
    """
    
def part_d():
    """
    
    We can ignore the middle cell and just split into cases due to rotational symmetry.
    
    Case middle cell is empty:
    Arrange in the configuration OOOOEEEE.
    We can swap any of the 'O' cells with any of the 'E' cells. We must divide by two for rotations. 
    Therefore we have 4x4 = 16 and then 16/2 = 8 ways.
    
    Case middle cell is either of two markers (WLOG, let the middle cell be O):
    This can be further split into the cases of the cells adjacent to the empty cell.
    Case OEO:
    5C1 - 1 = 4 ways due to one symetric case where the final O is placed next to one of the existing O's.
    Case XEO:
    This configuration locks the rotation so we can just count the number of ways to place the O's. This is 5C2 = 10 ways
    Case XEX:
    There are 5C2 ways to place the X's. We must divide by two to avoid double counting rotations. This is 5C2 / 2 = 5 ways.
    
    We must double the ways for the case where the middle cell is a marker because I assumed it was O at the start.
    Therefore, in total we have 8 + 2(4+10+5) = 8 + 2(19) = 46 ways in total.
    
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
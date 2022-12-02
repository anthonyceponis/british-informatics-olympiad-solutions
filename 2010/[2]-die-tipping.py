import time

"""
    
NOTES:

a)  
This problem was mainly just taking care of overflows and figuring out a nice way of representing the data and state of the game. 
It would have probably been better to use object oriented code in this case (using classes etc) but I decided to keep it simple by using dictionaries instead.
I did not use anything 'special' to answer this problem (e.g. some complicated matrix formulas), I just carefully chose how to perform rotations and move on the grid. 

"""

def play(dice, grid):
    grid[dice["y"]][dice["x"]] += dice["top"]
    num = grid[dice["y"]][dice["x"]]
    # Handle overflow
    if num > 6: 
        num -= 6
        grid[dice["y"]][dice["x"]] = num
    # Cases num == 1 and num == 6 require no extra manipulation
    if num == 2:
        dice = rotateHeading(dice, "R")
    elif num == 3 or num == 4:
        # Rotating twice in a direction is the same as the opposite direction (does not matter whether we rotate left or right, I just randomly chose right)
        dice = rotateHeading(dice, "R")
        dice = rotateHeading(dice, "R")
    elif num == 5: 
        dice = rotateHeading(dice, "L")

    # Dice must be rotated and moved in every case
    dice = rotateDice(dice)
    dice = move(dice)
    
    return dice
        
# Moves according to the state of the heading (which is why the heading must always be adjusted first)
def move(dice):
    x = dice["x"]
    y = dice["y"]
    if dice["heading"] == 0:
        # North
        y -= 1
    elif dice["heading"] == 1:
        # East
        x += 1
    elif dice["heading"] == 2:
        # South
        y += 1
    elif dice["heading"] == 3:
        # West
        x -= 1
    
    # Handle overflows for an 11x11 grid
    if x < 0: x += 11
    elif x > 10: x-= 11
    elif y < 0: y += 11
    elif y > 10: y-= 11
    
    dice["x"] = x
    dice["y"] = y
    
    return dice
    
# Rotates according to the current state of the header 
def rotateDice(dice):
    newDiceConfig = dice.copy()
    if dice["heading"] == 0:
        # North
        newDiceConfig["back"] = dice["top"]
        newDiceConfig["bottom"] = dice["back"]
        newDiceConfig["front"] = dice["bottom"]
        newDiceConfig["top"] = dice["front"]
    elif dice["heading"] == 1:
        # East
        newDiceConfig["left"] = dice["bottom"]
        newDiceConfig["bottom"] = dice["right"]
        newDiceConfig["right"] = dice["top"]
        newDiceConfig["top"] = dice["left"]
    elif dice["heading"] == 2:
        # South
        newDiceConfig["top"] = dice["back"]
        newDiceConfig["back"] = dice["bottom"]
        newDiceConfig["bottom"] = dice["front"]
        newDiceConfig["front"] = dice["top"]
    elif dice["heading"] == 3:
        # West
        newDiceConfig["bottom"] = dice["left"]
        newDiceConfig["right"] = dice["bottom"]
        newDiceConfig["top"] = dice["right"]
        newDiceConfig["left"] = dice["top"]
    
    return newDiceConfig
        
        

# direction is 'L' or 'R' representing left and right respectively which are also the same as anti-clockwise and clockwise respectively
def rotateHeading(dice, direction):
    if direction == "L": dice["heading"] -= 1
    elif direction == "R": dice["heading"] += 1
    if dice["heading"] < 0: dice["heading"] += 4
    elif dice["heading"] > 3: dice["heading"] -= 4
    return dice
    
def displayGrid(dice, grid):
    for y_offset in range(-1, 2):
        row = ""
        for x_offset in range(-1, 2):
            y = dice["y"] + y_offset
            x = dice["x"] + x_offset
            if y > 10 or y < 0 or x > 10 or x < 0: 
                row += "X"
            else: 
                row += str(grid[y][x])
        print(row)
    
# heading is represented by an index of the following array: [north, east, south and west]
def part_a():
    dice = {"left": 3, "right": 4, "top": 1, "bottom": 6, "back": 2, "front": 5, "heading": 0, "x": 5, "y": 5}
    grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] for x in range(11)]
        
    for i in range(3):
        row = [int(x.strip()) for x in input().split(" ")]
        grid[4+i][4] = row[0]
        grid[4+i][5] = row[1]
        grid[4+i][6] = row[2]
        
    n = 1
    while n > 0:
        n = int(input())
        for i in range(n):
            dice = play(dice, grid)
        print()
        if n != 0:
            displayGrid(dice, grid)

def part_b():
    """
    
    The first move must yield a 2 so that the dice would rotate 90deg clockwise so the first middle square must be a 1.
    The next squares must sum with the top of the dice to form a 3 or 4 so there are 2 choices for the remaining 5 squares (before tipping over the right edge).
    This is 2^5 = 32 ways
    
    """

def part_c():
    """
    
    By uppermost I presume it means the face that is vertically opposite to the face in contact with the board (the face on the top).
    There are two 'types' of tippings. One is where the dice goes out in the same direction twice but this would result in the uppermost face being the same.
    The other is where it kind of rolls around e.g. south, west, north, east. 
    Clearly, there are 4 direction where the tipping can start from and for each of those there 2 directions is can tip. The other two tips are fixed since it must return to the same position.
    This means there are 4 * 2 = 8 ways using 4 tips.
    
    You can solve the 6 tips case by considering the 4 tips case. 
    For 6 tips, you need 4 good tips with an additional 2 good tips.
    So first we must choose a pair of moves that cancel. There are 2 such pairs: (up, down) and (left, right). Each pair can also be in any order.
    This makes a total of 2 * 2 = 4 pairs.
    The items in these pairs must be directly next to each other so there are 5 places they can be put in the sequence of 6 moves.
    The rest of the sequence can be filled with any of the valid sequences for 4 tips. 
    This yields a final answer of 4 * 5 * 8 = 160.
    
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
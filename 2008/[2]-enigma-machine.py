import time
import itertools

"""
    
NOTES:

a)
I have tried my best to explain what I am doing throughout the code as it made more sense to explain along the way rather than as a summary at the start.  

"""

# rotor (to rotate) can be either "L" or "R" representing left and right respectively
# I will represent the connections of the left rotor as the offset index from the left port to the right port
# For the right rotor, I will represent connections as the offset index from the right port to the left port
# e.g. in the example given (in the initial state), the left rotor will be represented as [0, -2, 1, 1] because the connection to the port from the left 'A' port is offset by 0 positions, from left 'B' is -2 etc.
# machine (matrix-like object) contains the left rotor as an array in index 0 and the right rotor as an array in index 1
# I will also include a dummy cell at the end of each matrix to make rotations easier
def rotate(rotor, machine):
    dummyCell = 4
    
    # Determine which rotor to rotate
    if rotor == "L":
        rotor = 0
    elif rotor == "R":
        rotor = 1
        
    # Here I am sending the connection at port A to the back in the dummy cell, then shifting all connections to the front of the the array
    machine[rotor][dummyCell] = machine[rotor][0]
    for i in range(1, 5):
        machine[rotor][i-1] = machine[rotor][i]
    machine[rotor][dummyCell] = None
    
def encrypt(machine, letter, singleRotor = False):
    letterIndex = ord(letter) - 65
    
    # Route through first rotor and adjust bounds
    letterIndex += machine[0][letterIndex]
    if letterIndex < 0: letterIndex += 4
    elif letterIndex > 3: letterIndex -= 4
    
    if not singleRotor:
        # Route through second rotor and adjust bounds
        letterIndex += machine[1][letterIndex]
        if letterIndex < 0: letterIndex += 4
        elif letterIndex > 3: letterIndex -= 4
    
    # Reflect
    reflection = [3, 2, 1, 0]
    letterIndex = reflection[letterIndex]
    
    if not singleRotor:
        # Route back through the second rotor
        for i in range(0, 4):
            reversedIndex = i
            reversedIndex += machine[1][reversedIndex]
            if reversedIndex < 0: reversedIndex += 4
            elif reversedIndex > 3: reversedIndex -= 4
            if reversedIndex == letterIndex:
                letterIndex = i
                break
    
    # Route back through the first rotor
    for i in range(0, 4):
        reversedIndex = i
        reversedIndex += machine[0][reversedIndex]
        if reversedIndex < 0: reversedIndex += 4
        elif reversedIndex > 3: reversedIndex -= 4
        if reversedIndex == letterIndex:
            letterIndex = i
            break
        
    return chr(letterIndex + 65)

def getCipherText(letters, lettersEncrypted):
    initialMachine = [[0, 2, -1, -1, 0], [0, 1, -1, 0, 0]]
    machine = initialMachine
    encrypted = ""
    
    # Must pre-rotate according to how many letters have already been encrypted
    # We can take advantage of modulo 4 in the case that there are big input sizes for pre-rotations
    for i in range(0, lettersEncrypted % 4):
        rotate("L", machine)
    for i in range(0, int((lettersEncrypted - (lettersEncrypted % 4)) / 4) % 4):
        rotate("R", machine)
    # Encrypt the word
    for letter in letters:
        cipherLetter = encrypt(machine, letter)
        encrypted += cipherLetter
        lettersEncrypted += 1
        rotate("L", machine)
        if (lettersEncrypted % 4 == 0):
            rotate("R", machine)
    
    return encrypted
    
def part_a():
    lettersEncrypted = int(input())
    letters = input()
    cipherText = getCipherText(letters, lettersEncrypted)
    print(cipherText)

def part_b():
    cipherText = getCipherText("AAAAAA", 0)
    print(cipherText)

def part_c():
    # Counting the number of valid ways using a single rotor
    singleRotorWays = 0
    perms = list(itertools.permutations([0, 1, 2, 3]))
    diffPerms = []
    for i in perms:
        diffPerms.append([i[0] - 0, i[1] - 1, i[2] - 2, i[3] - 3, 0])
    
    for i in diffPerms:
        machine = [i]
        valid = True
        for j in range(4):
            if encrypt(machine, "A", True) != "B" or encrypt(machine, "B", True) != "A" or encrypt(machine, "C", True) != "D" or encrypt(machine, "D", True) != "C":
                valid = False
                break
            rotate("L", machine)
        if valid: singleRotorWays += 1
    print(singleRotorWays)
    
    # Counting the number of valid ways using a double rotor
    doubleRotorWays = 0
    perms = list(itertools.permutations([0, 1, 2, 3]))
    diffPerms = []
    for i in perms:
        diffPerms.append([i[0] - 0, i[1] - 1, i[2] - 2, i[3] - 3, 0])
    doubleDiffPerms = []
    for i in diffPerms:
        doubleDiffPerms.append([i, diffPerms])
    
    # I did using range 16 this time because we must also count the cases where we rotate the second rotor which happens every 4 so we must do 4x4
    for i in doubleDiffPerms:
        for j in i[1]:
            machine = [i[0][:], j[:]]
            valid = True
            for j in range(16):
                if encrypt(machine, "A") != "B" or encrypt(machine, "B") != "A" or encrypt(machine, "C") != "D" or encrypt(machine, "D") != "C":
                    valid = False
                    break
                rotate("L", machine)
                if (j + 1) % 4 == 0:
                    rotate("R", machine)
            if valid: doubleRotorWays += 1
    print(doubleRotorWays)
    
def part_d():
    """
    
    Every letter is part of a single loop and connects to a single port on the other side of the rotor. 
    If A encrypts to B and B encrypts to C, this means B is part of two loops which is impossible and is therefore a contradiction.
    If A encrypts to B then B must encrypt back to A, otherwise it would be almost impossible to consistently encrypt/decrypt letters.
    Therefore, it is not possible. 
    
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
import time

"""
    
NOTES:

a)
I feel like this problem was actually on the easier side. 
The difficulty is in the ammount of information given and writing the solution quickly since it is quite long.
As the problem suggested, I split my program into the three different strats with a few helper functions.
I think that if you understand the problem completely then the implementation is not complicated which is why I won't go into too much detail about it.

b)
This was just another easy 2 marks by calling the shuffle algorithm from part a with a specific input

c)
Here you have to realise that this question is equivalent to asking: "How many ways can you sum to 52 using six numbers in between 1 and 9?"
Then the question is just brute force.

"""

def makeMove(deck, pileTracker, srcIndex, destIndex):
    deck[destIndex] = deck[srcIndex]
    pileTracker[destIndex] += pileTracker[srcIndex]
    del deck[srcIndex]
    del pileTracker[srcIndex]

# Returns True if a move was made, signifying that the game is not yet over. If it returns False then it means there are no more moves to be made using this stratergy.
def strat1(deck, pileTracker):
    for rightMostPossibleIndex in range(len(deck)-1, 0, -1):
        i = rightMostPossibleIndex - 1
        j = rightMostPossibleIndex - 3
        if i >= 0 and (list(deck[i])[0] == list(deck[rightMostPossibleIndex])[0] or list(deck[i])[1] == list(deck[rightMostPossibleIndex])[1]):
            makeMove(deck, pileTracker, rightMostPossibleIndex, i)
            return True
        elif j >= 0 and (list(deck[j])[0] == list(deck[rightMostPossibleIndex])[0] or list(deck[j])[1] == list(deck[rightMostPossibleIndex])[1]):
            makeMove(deck, pileTracker, rightMostPossibleIndex, j)
            return True
    return False

def strat2(deck, pileTracker):
    largestPilePossible = 1
    srcIndex = None
    destIndex = None
    for rightMostPossibleIndex in range(len(deck)-1, 0, -1):
        i = rightMostPossibleIndex - 1
        j = rightMostPossibleIndex - 3
        if i >= 0 and (list(deck[i])[0] == list(deck[rightMostPossibleIndex])[0] or list(deck[i])[1] == list(deck[rightMostPossibleIndex])[1]):
            currentPile = pileTracker[i] + pileTracker[rightMostPossibleIndex]
            if currentPile > largestPilePossible:
                largestPilePossible = currentPile
                srcIndex = rightMostPossibleIndex
                destIndex = i
        if j >= 0 and (list(deck[j])[0] == list(deck[rightMostPossibleIndex])[0] or list(deck[j])[1] == list(deck[rightMostPossibleIndex])[1]):
            currentPile = pileTracker[j] + pileTracker[rightMostPossibleIndex]
            if currentPile > largestPilePossible:
                largestPilePossible = currentPile
                srcIndex = rightMostPossibleIndex
                destIndex = j
    if srcIndex != None and destIndex != None:
        makeMove(deck, pileTracker, srcIndex, destIndex)
        return True
    return False

def countMoves(deck):
    validMoves = 0
    for rightMostPossibleIndex in range(len(deck)-1, 0, -1):
        i = rightMostPossibleIndex - 1
        j = rightMostPossibleIndex - 3
        if i >= 0 and (list(deck[i])[0] == list(deck[rightMostPossibleIndex])[0] or list(deck[i])[1] == list(deck[rightMostPossibleIndex])[1]):
            validMoves += 1
        if j >= 0 and (list(deck[j])[0] == list(deck[rightMostPossibleIndex])[0] or list(deck[j])[1] == list(deck[rightMostPossibleIndex])[1]):
            validMoves += 1
    return validMoves


def strat3(deck, pileTracker):
    largestValidMoves = -1
    srcIndex = None
    destIndex = None
    for rightMostPossibleIndex in range(len(deck)-1, 0, -1):
        i = rightMostPossibleIndex - 1
        j = rightMostPossibleIndex - 3
        if i >= 0 and (list(deck[i])[0] == list(deck[rightMostPossibleIndex])[0] or list(deck[i])[1] == list(deck[rightMostPossibleIndex])[1]):
            tempDeck = deck[:]
            tempPileTracker = pileTracker[:]
            makeMove(tempDeck, tempPileTracker, rightMostPossibleIndex, i)
            currentMoves = countMoves(tempDeck)
            if currentMoves > largestValidMoves:
                largestValidMoves = currentMoves
                srcIndex = rightMostPossibleIndex
                destIndex = i
        if j >= 0 and (list(deck[j])[0] == list(deck[rightMostPossibleIndex])[0] or list(deck[j])[1] == list(deck[rightMostPossibleIndex])[1]):
            tempDeck = deck[:]
            tempPileTracker = pileTracker[:]
            makeMove(tempDeck, tempPileTracker, rightMostPossibleIndex, j)
            currentMoves = countMoves(tempDeck)
            if currentMoves > largestValidMoves:
                largestValidMoves = currentMoves
                srcIndex = rightMostPossibleIndex
                destIndex = j
    if srcIndex != None and destIndex != None:
        makeMove(deck, pileTracker, srcIndex, destIndex)
        return True
    return False
        
        
def shuffleDeck(deck, shuffleInts):
    tempDeck = deck[:]
    shuffledDeck = []
    currentShuffleIntsIndex = 0
    currentDeckIndex = -1
    while len(shuffledDeck) < 52:
        currentDeckIndex = (currentDeckIndex + shuffleInts[currentShuffleIntsIndex]) % len(tempDeck)
        shuffledDeck.append(tempDeck[currentDeckIndex])
        del tempDeck[currentDeckIndex]
        currentDeckIndex -= 1
        currentShuffleIntsIndex = (currentShuffleIntsIndex + 1) % len(shuffleInts)
    return shuffledDeck

def part_a():
    shuffleInts = [int(x.strip()) for x in input().split(" ")]
    deck = []
    pileTracker = [1 for i in range(52)]
    suits = ["C", "H", "S", "D"]
    values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K"]
    for suit in range(4):
        for value in range(13):
            deck.append(str(values[value]) + suits[suit])

    
    shuffledDeck = shuffleDeck(deck, shuffleInts)
    pileTracker = [1 for i in range(52)]
    print()
    print(shuffledDeck[0], shuffledDeck[-1])
    while strat1(shuffledDeck, pileTracker):
        pass
    print(len(shuffledDeck), shuffledDeck[0])
    shuffledDeck = shuffleDeck(deck, shuffleInts)
    pileTracker = [1 for i in range(52)]
    while strat2(shuffledDeck, pileTracker):
        pass
    print(len(shuffledDeck), shuffledDeck[0])
    shuffledDeck = shuffleDeck(deck, shuffleInts)
    pileTracker = [1 for i in range(52)]
    while strat3(shuffledDeck, pileTracker):
        pass
    print(len(shuffledDeck), shuffledDeck[0])
    
    
def part_b():
    shuffleInts = [2, 11, 3, 10, 4, 9]
    deck = []
    pileTracker = [1 for i in range(52)]
    suits = ["C", "H", "S", "D"]
    values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K"]
    for suit in range(4):
        for value in range(13):
            deck.append(str(values[value]) + suits[suit])

    
    shuffledDeck = shuffleDeck(deck, shuffleInts)
    print(" ".join(shuffledDeck[:12]))
    
def part_c():
    for i in range(2):
        ways = 0
        for target in range(6, 53):
            for a in range(1, 10 + i):
                if a > target:
                    break
                for b in range(1, 10 + i):
                    if a + b > target:
                        break
                    for c in range(1, 10 + i):
                        if a + b + c > target:
                            break
                        for d in range(1, 10 + i):
                            if a + b + c + d > target:
                                break
                            for e in range(1, 10 + i):
                                if a + b + c + d + e > target:
                                    break
                                for f in range(1, 10 + i):
                                    if a + b + c + d + e + f > target:
                                        break
                                    if a + b + c + d + e + f == target:
                                        ways += 1
        print(ways)

def part_d():
    """
    
    Check official solution.
    
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
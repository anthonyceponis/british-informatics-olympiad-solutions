import time

"""
    
NOTES:

a)  
The challenge in this problem was coming up with a good data structure for the simulation.
I decided to keep it simple using a dictionary and the rest is nothing special and more or less translating the logic given in the question line by line.
I have annotated my code where possible to explain what I am doing.

"""

def simulateStep(track, fr, to):
    # Entering on a straight track, otherwise from a curved track
    if track[to]["straight"] == fr:
        # Update the fr and to pointers
        fr = to
        if track[to]["direction"] == "L":
            to = track[to]["left"]
        elif track[to]["direction"] == "R":
            to = track[to]["right"]
        
        # Switch the direction if the point is flipflop since we are entering from a straight track
        if track[fr]["point"] == "FF":
            if track[fr]["direction"] == "L":
                track[fr]["direction"] = "R"
            elif track[fr]["direction"] == "R":
                track[fr]["direction"] = "L"
    else:
        prev = fr
        fr = to
        to = track[to]["straight"]
        
        # Update direction if the point is lazy since we are entering from a curved track
        if track[fr]["point"] == "L":
            if track[fr]["left"] == prev:
                track[fr]["direction"] = "L"
            elif track[fr]["right"] == prev:
                track[fr]["direction"] = "R"
    
    return [track, fr, to]

def part_a():
    # point can be set to L (lazy) or FF (flip-flop)
    # direction can be set to L (left) or R (right)
    track = {
        "A": {
            "straight": "D",
            "left": "E",
            "right": "F",
            "point": "L",
            "direction": "L"
        },
        "B": {
            "straight": "C",
            "left": "G",
            "right": "H",
            "point": "L",
            "direction": "L"
        },
        "C": {
            "straight": "B",
            "left": "I",
            "right": "J",
            "point": "L",
            "direction": "L"
        },
        "D": {
            "straight": "A",
            "left": "K",
            "right": "L",
            "point": "L",
            "direction": "L"
        },
        "E": {
            "straight": "A",
            "left": "M",
            "right": "N",
            "point": "L",
            "direction": "L"
        },
        "F": {
            "straight": "A",
            "left": "N",
            "right": "O",
            "point": "L",
            "direction": "L"
        },
        "G": {
            "straight": "B",
            "left": "O",
            "right": "P",
            "point": "L",
            "direction": "L"
        },
        "H": {
            "straight": "B",
            "left": "P",
            "right": "Q",
            "point": "L",
            "direction": "L"
        },
        "I": {
            "straight": "C",
            "left": "Q",
            "right": "R",
            "point": "L",
            "direction": "L"
        },
        "J": {
            "straight": "C",
            "left": "R",
            "right": "S",
            "point": "L",
            "direction": "L"
        },
        "K": {
            "straight": "D",
            "left": "S",
            "right": "T",
            "point": "L",
            "direction": "L"
        },
        "L": {
            "straight": "D",
            "left": "T",
            "right": "M",
            "point": "L",
            "direction": "L"
        },
        "M": {
            "straight": "U",
            "left": "L",
            "right": "E",
            "point": "L",
            "direction": "L"
        },
        "N": {
            "straight": "U",
            "left": "E",
            "right": "F",
            "point": "L",
            "direction": "L"
        },
        "O": {
            "straight": "V",
            "left": "F",
            "right": "G",
            "point": "L",
            "direction": "L"
        },
        "P": {
            "straight": "V",
            "left": "G",
            "right": "H",
            "point": "L",
            "direction": "L"
        },
        "Q": {
            "straight": "W",
            "left": "H",
            "right": "I",
            "point": "L",
            "direction": "L"
        },
        "R": {
            "straight": "W",
            "left": "I",
            "right": "J",
            "point": "L",
            "direction": "L"
        },
        "S": {
            "straight": "X",
            "left": "J",
            "right": "K",
            "point": "L",
            "direction": "L"
        },
        "T": {
            "straight": "X",
            "left": "K",
            "right": "L",
            "point": "L",
            "direction": "L"
        },
        "U": {
            "straight": "V",
            "left": "M",
            "right": "N",
            "point": "L",
            "direction": "L"
        },
        "V": {
            "straight": "U",
            "left": "O",
            "right": "P",
            "point": "L",
            "direction": "L"
        },
        "W": {
            "straight": "X",
            "left": "Q",
            "right": "R",
            "point": "L",
            "direction": "L"
        },
        "X": {
            "straight": "W",
            "left": "S",
            "right": "T",
            "point": "L",
            "direction": "L"
        },
    }
    
    ffpoints = list(input())
    for i in ffpoints:
        track[i]["point"] = "FF"
    cin = list(input())
    fr = cin[0]
    to = cin[1]
    steps = int(input())
    
    for i in range(steps):
        result = simulateStep(track, fr, to)
        track = result[0]
        fr = result[1]
        to = result[2]
    
    print(fr + to)
    
def part_b():
    """
    
    For this question I will just look at the diagram given and trace the journey.
    Starts at P and is going to V. 
    V then must go to U (since it was entered from a curved track) and set to right since it is lazy and we entered from the right.
    U then must go to M since all points are lazy and are set to left and we came into U from a straight track.
    M then must go to L by the same logic as the previous node.
    L must go to D since we entered from a curved track and set to right.
    D must go to A since we enetered from a curved and set to right.
    A must go to E since we entered from a straight and A is initially set to left since all points are lazy.
    E must go to M since by the same logic as the previous node.
    M must go to U since we entered from a curved track.
    U must go V since we entered U from a curved track.
    V now goes to P since it was set to right originally.
    
    So the final sequence is P, V, U, M, L, D, A, E, M, U, V, P.
    
    """
    
def part_c():
    """
    
    So I feel like the wording of this question is not specific enough (might just be me though) because I thought the question wants us to determine the exact position but after reading the mark scheme, it only wants the 'level' that it is on.
    Since this question is a bit weird, I will explain their answer as well just in case.
    So they grouped the nodes into levels: A,B,C,D get grouped into 1 level called A-D; E,F,G,H,I,J,K,L get grouped into another level called E-L; the other levels are M-T and U-X bt the same logic.
    Then it is fairly easy to see that if the train has just entered level U-X from level M-T, then it will remain on U-X, then go to M-T, then to E-L etc.
    There is a good diagram on the official mark scheme which you should check out.
    In total, there are 8 types of transitions before looping to the same set of transitions.
    p->v is equivalent to moving from level M-T to level U-X and that big number is divisible by 8 (which is obvious since it is divisible by 10 loads of times which has a factor of 2 which also implies it is divisible by 8 loads of times).
    This means we will end up back at the same level transition of M-T to U-X.
    
    """
    
def part_d():
    """
    
    Not sure. If you have a explanation then please raise an issue on the repo and I will add a credited solution.
    
    """
    


def main():
    startTime = time.time()
    
    part_a()

    print(f'Execution time (seconds): {round(time.time() - startTime, 5)}')
    pass

if __name__ == "__main__":
    main()
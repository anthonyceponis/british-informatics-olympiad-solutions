import time

"""
    
NOTES:

a)
Here is just used integer division and modular arithmetic for checking the equality of two times on the clock.  

b)
This just reuses the function made in part a and enumerates over possible offsets for the second clock

c)
I just iterated through all the possible minutes fast (mod 60) and found the maximum hours passed (actual hours rather than the hours shown on the clocks)

"""

def getTimeFirstMatch(time1Fast, time2Fast, hourDif = False):
    time1 = 60 + time1Fast
    time2 = 60 + time2Fast
    hoursPassed = 1
    while (time1 % 60 != time2 % 60 or (time1 // 60) % 24 != (time2 // 60) % 24):
        time1 += 60 + time1Fast
        time2 += 60 + time2Fast
        hoursPassed += 1
    hours = (time1 // 60) % 24
    mins = time1 % 60
    if (len(str(hours)) == 1): hours = "0" + str(hours)
    if (len(str(mins)) == 1): mins = "0" + str(mins)
    if (hourDif): return hoursPassed
    return f'{hours}:{mins}'

def part_a():
    with open("(1)-test.txt", "r") as f:
        content = f.readlines()
        for line in content:
            cin = line.split(" ")[0:2]
            expected = line.split(" ")[-1].strip()
            cout = getTimeFirstMatch(int(cin[0]), int(cin[1]))
            status = "failed"
            if (cout == expected): status = "passed"
            print(f'status: {status} ||| input: {cin} ||| output: {cout} ||| expected: {expected}')

def part_b():
    possible = set()
    for i in range(0, 20):
        match = getTimeFirstMatch(0, i)
        if (match != "00:00"): possible.add(i)
    for i in possible:
        print(i)

def part_c():
    maxHourDif = 0
    for offset1 in range(0, 59):
        for offset2 in range(0, 59):
            maxHourDif = max(maxHourDif, abs(getTimeFirstMatch(offset1, offset2, True)))
    print(maxHourDif)

def main():
    startTime = time.time()
    
    # part_a()
    # part_b()
    # part_c()

    print(f'Execution time (seconds): {round(time.time() - startTime, 5)}')
    pass

if __name__ == "__main__":
    main()
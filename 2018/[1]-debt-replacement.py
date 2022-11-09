import time
import math

"""

a)
A simple iterative algorithm that simply translates the instructions in the question.
Key trick was multiply everything by 100 and work with ints as much as possible 
and then divide at the end to avoid rounding errors.

b)
Simply adds a step tracker to part a

c)
Simply brute force but I had to update the method in part a to check that the debt is strictly decreasing.
Otherwise, the debt would be diverging and not possible to pay off.


"""

def repaid(interestP, repaymentP, debt, paid, countSteps = False, steps = 0):
    while (0 < debt):
        interest = math.ceil(debt * interestP)
        debt += interest
        repayment = min(max(math.ceil(debt * repaymentP), 5000), debt)
        paid += repayment
        debt -= repayment
        steps += 1
        if (debt >= 10000): break
        
    steps = 0
    if (countSteps): return steps 
    elif (debt == 0):
        return paid / 100
    else: return 0
    

def part_a():
    # For manual input
    # cin = input()
    # interestP = int(cin.split(" ")[0].strip())
    # repaymentP = int(cin.split(" ")[1].strip())
    
     with open("(1)-test.txt", "r") as f:
        content = f.readlines()
        for line in content:
            interestP = float(line.split(" ")[0].strip()) / 100
            repaymentP = float(line.split(" ")[1].strip()) / 100
            expected = float(line.split(" ")[2].strip()) 
            debt = 10000.0
            paid = 0.0
            status = "failed"
            out = repaid(interestP, repaymentP, debt, paid)
            if (out == expected): status = "passed"
            print(f'status: {status} ||| input: {interestP} {repaymentP} ||| output: {out} ||| expected: {expected}')
            
def part_b():
    interestP = 0.43
    repaymentP = 0.46
    debt = 10000.0
    paid = 0.0
    out = repaid(interestP, repaymentP, debt, paid, True)
    print(out)
    
def part_c():
    highestRepaid = 0
    sol_interest = 0
    sol_repayment = 0
    debt = 10000.0
    paid = 0.0
    for interestP in range(101):
        for repaymentP in range(101):
            out = repaid(interestP / 100, repaymentP / 100, debt, paid)
            if (out > highestRepaid): 
                highestRepaid = out
                sol_interest = interestP
                sol_repayment = repaymentP
    
    print(sol_interest / 100)
    print(sol_repayment / 100)

def main():
    startTime = time.time()
    
    # part_a()
    # part_b()
    # part_c()

    print(f'Execution time (seconds): {round(time.time() - startTime, 5)}')
    pass

if __name__ == "__main__":
    main()
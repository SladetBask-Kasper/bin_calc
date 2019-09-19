from os import system
from sys import argv
def calc(stop = 20):
    i = 1
    x = 1
    done = False
    while not done:
        if x >= stop:
            done = True
        print("["+str(x)+"]\t"+str(i))
        i = i*2
        x += 1
def slow_catch(stop = 20):
    i = 1
    x = 1
    while True:
        if x >= stop:
            return i
        i = i*2
        x += 1
def solve(num = "10010011"):
    num = num[::-1]
    x = 1
    rv = 0
    for let in num:
        if let == "1":
            rv += slow_catch(x)
        x += 1
    return rv
try:
    if argv[1]:
        pass
except:
    calc()
else:
    try:
        calc(int(argv[1]))
    except:
        if argv[1] == "catch":
            print(int(argv[2])**2)
        elif argv[1] == "slowcatch":
            print(slow_catch(int(argv[2])))
        elif argv[1] == "solve":
            print(solve(str(argv[2])))
        else:
            print("whut")
system("pause")

###
###
###
"""
10010001
128 + 16 + 1
"""

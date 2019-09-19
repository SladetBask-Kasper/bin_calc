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
try:
    calc(int(argv[1]))
except:
    calc()
system("pause")

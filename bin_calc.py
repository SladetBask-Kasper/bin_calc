from os import system
from sys import argv
from string import ascii_lowercase as alp

### KEY CODES
LOWCASE_ASCII = "011"
UPRCASE_ASCII = "010"
SPECIAL_CHAR  = "001"
UNUSUAL_CHAR  = "101"


###
### Draws a table of all the values from diffrent posistions
###
def table(stop = 20):
    i = 1
    x = 1
    done = False
    while not done:
        if x >= stop:
            done = True
        print("["+str(x)+"]\t"+str(i))
        i = i*2
        x += 1
def catch(stop = 20):
    return 2**(int(stop)-1)
###
### The same as above except it doesn't print anything and returns value. Preferable this would be a mathematical function.
###
def slow_catch(stop = 20):
    i = 1
    x = 1
    while True:
        if x >= stop:
            return i
        i = i*2
        x += 1

###
### calculate an array of values
###
def mass_calc(arr):
    rv = 0
    for ind in arr:
        rv += catch(int(ind))
    return rv
###
### calculate an array of values
###
def slow_mass_calc(arr):
    rv = 0
    for ind in arr:
        rv += slow_catch(int(ind))
    return rv
###
### Bin to decimal
###
def solve(num = "10010011"):
    num = num[::-1]
    x = 1
    rv = 0
    for let in num:
        if let == "1":
            rv += catch(x)
        x += 1
    return rv
###
###
###
def calc(nums):
    return bin(nums)[2:].zfill(8)
###
### Bin to text
###
def txt(bine):
    bin_lets = [bine[i:i+8] for i in range(0, len(bine), 8)] #splits string every 8 char
    rv = ""
    for let in bin_lets:
        s = solve(let[3:]) ### Remove first three since they have nothing to do with value rv
        try:
            rv += alp[s-1]
        except:
            print("letter out of range")
    return rv
###
### Text to bin
###
def bny(text):
    rv = ""
    specialKey = False
    for let in list(text):

        if let == "{" and not specialKey:
            specialKey = True
            continue
        elif let == "{" and specialKey:
            rv += "01111011"
            specialKey = False
            continue

        bchar = LOWCASE_ASCII
        if let.isupper():
            bchar = UPRCASE_ASCII
        if let == "_" and not specialKey:
            rv += "00100000"
            continue
        if let == "_" and specialKey:
            rv += "01011111"
            specialKey = False
            continue
        i = "?"# Error char as default
        try:
            i = alp.index(let.lower())+1
        except:
            print("unknown character")
        rv += bchar + calc(i)[3:]
    return rv







try:
    if argv[1]:
        pass
except:
    table()
    print("Add argument \"help\" to get help menu")
    system("pause")
else:
    try:
        table(int(argv[1]))
    except:
        if argv[1] == "catch":
            print(catch(int(argv[2])))
        elif argv[1] == "slowcatch":
            print(slow_catch(int(argv[2])))
        elif argv[1] == "solve":
            print(solve(str(argv[2])))
        elif argv[1] == "calc":
            print(calc(int(argv[2])))
        elif argv[1] == "bintotext":
            print(txt(str(argv[2])))
        elif argv[1] == "texttobin":
            print(bny(str(argv[2])))
        elif argv[1] == "masscalc":
            arr = []
            x = 2
            while x < len(argv):
                arr.append(argv[x])
                x += 1
            print(mass_calc(arr))
        elif argv[1] == "slowmasscalc":
            arr = []
            x = 2
            while x < len(argv):
                arr.append(argv[x])
                x += 1
            print(slow_mass_calc(arr))
        else:
            print("catch [num] - get number on posistion")
            #print("slowcatch [num] - get number on posistion by loop")
            print("solve [bin_num] - bin to decimal")
            print("calc [decimal] - decimal to bin")
            print("masscalc [array of numbers] - calculates all args decimal to bin_worth combined")
            print("bintotext [bin_txt] - bin to text")
            print("texttobin [txt] - text to bin")
            system("pause")

"""
10010001
128 + 16 + 1
"""

import os

username = os.getlogin()

path = r'C:\Users\'' + username + r'\Downloads'

os.chdir(path.replace("'", ""))
import codecs
import time

msg = input("Enter file name here: ")

start = time.time()

with codecs.open(msg + ".txt", 'r', 'utf-8-sig', 'ignore') as f:
    data = f.read()

lines = data.split("\n" + "")

lst = []

for line in lines:
    if len(line) > 1:
        lst.append(line.rstrip("\r"))

newLst = []

for i in range(0, len(lst)):
    if lst[i][0] == "[" and lst[i][0:4].__contains__("/") == True:
        first_colon = lst[i].index(":")
        second_colon = lst[i].index(":", (first_colon+1))
        xxx = second_colon + 2
        intro_stripped = lst[i][xxx:]
    else:
        intro_stripped = lst[i]
    newLst.append(intro_stripped)

for i in range(0, len(newLst)):
    if newLst[i].__contains__("⁨"):
        newLst[i] = newLst[i].replace("⁨", "")

for i in range(0, len(newLst)):
    if newLst[i].__contains__("⁩"):
        newLst[i] = newLst[i].replace("⁩", "")

def IsEven(num):
    if num == 0:
        result = False
    elif num % 2 == 0:
        result = True
    else:
        result = False
    return result

for i in range(0, len(newLst)):
    asterisks = newLst[i].count("*")
    astEven = IsEven(asterisks)

    if astEven:
        startpos = 0
        for xix in range(0, int(asterisks / 2)):
            length = len(newLst[i])
            first_ast = newLst[i].index("*", startpos)
            second_ast = newLst[i].index("*", (first_ast + 1))
            if second_ast < (length - 1):
                newLst[i] = newLst[i][0:first_ast] + "<b>" + newLst[i][(first_ast + 1):second_ast] + "</b>" + newLst[i][(second_ast+1):]
            elif second_ast == (length - 1):
                newLst[i] = newLst[i][0:first_ast] + "<b>" + newLst[i][(first_ast + 1):second_ast] + "</b>"
            startpos = (second_ast + 1)

for i in range(0, len(newLst)):
    underscore = newLst[i].count("_")
    undEven = IsEven(underscore)

    if undEven:
        startpos = 0
        for xix in range(0, int(underscore / 2)):
            length1 = len(newLst[i])
            first_und = newLst[i].index("_", startpos)
            second_und = newLst[i].index("_", (first_und + 1))
            if second_und < (length1 - 1):
                newLst[i] = newLst[i][0:first_und] + "<i>" + newLst[i][(first_und + 1):second_und] + "</i>" + newLst[i][(second_und + 1):]
            elif second_und == (length1 - 1):
                newLst[i] = newLst[i][0:first_und] + "<i>" + newLst[i][(first_und + 1):second_und] + "</i>"
            startpos = (second_und + 1)

for i in range(0, len(newLst)):
    spacewrite = newLst[i].count("```")
    spaceEven = IsEven(spacewrite)

    if spaceEven:
        startpos = 0
        for xix in range(0, int(spacewrite / 2)):
            length2 = len(newLst[i])
            first_und = newLst[i].index("```", startpos)
            second_und = newLst[i].index("```", (first_und + 3))
            if second_und < (length2 - 1):
                newLst[i] = newLst[i][0:first_und] + newLst[i][(first_und + 3):second_und] + newLst[i][(second_und + 3):]
            elif second_und == (length2 - 1):
                newLst[i] = newLst[i][0:first_und] + newLst[i][(first_und + 3):second_und]
            startpos = (second_und + 3)

for i in range(0, len(newLst)):
    strikethru = newLst[i].count("~")
    strEven = IsEven(strikethru)

    if strEven:
        startpos = 0
        for xix in range(0, int(strikethru / 2)):
            length3 = len(newLst[i])
            first_und = newLst[i].index("~", startpos)
            second_und = newLst[i].index("~", (first_und + 1))
            if second_und < (length3 - 1):
                newLst[i] = newLst[i][0:first_und] + "<s>" + newLst[i][(first_und + 1):second_und] + "</s>" + newLst[i][(second_und + 1):]
            elif second_und == (length3 - 1):
                newLst[i] = newLst[i][0:first_und] + "<s>" + newLst[i][(first_und + 1):second_und] + "</s>"
            startpos = (second_und + 1)

Edited = msg.replace(".txt", "")
newfile = Edited + " [Filtered]" + ".doc"

with codecs.open(newfile, 'w', 'utf-8-sig', 'ignore') as fv:
    fv.write("<html><head></head><body>" + "\n")
    for line in newLst:
        fv.write(str(line) + "<br><br>" + "\n")
    fv.write("</body></html>")

fv.close()

print("JOB DONE!")
exit_code_00 = input("Press any key to exit: ")
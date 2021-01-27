#Regex version of strip()
#21.09.2019
#22.09.2019 Refactored (1)

"""noun: a change made to the internal structure of software to make it easier
to understand and cheaper to modify without changing its observable behavior

verb: to restructure software by applying a series of refactorings without
changing its observable behavior."""

import re, pyperclip, time

stuff = "oomenips "
stuff1 = "0311MOS033"
stuff2 = "booyakasha"
stuff3 = "    Title   "

print(stuff, stuff1, stuff2, stuff3, end= ' ')
time.sleep(0.3)
print()

def stripRe(randStr, elim = " "): #Default value of item to remove is blankspace
        time.sleep(0.4)
        print("Item to be stripped from '%s' is '%s'."%(randStr, elim))
        newStr = list()
        elimList = list() #create list of items to be deleted
        finalStr = str() #this will be the collated form of the string, i.e. the final string output
        for k in randStr:
            newStr.append(k)
        for e in elim:
            elimList.append(e)   
            #print(elimList) #D
        #print("System will strip the following:", toStrip)#D
        for m in elimList:
            elimRe = re.compile(m)
            toStrip = elimRe.findall(randStr)
            stripLen = int()
            for r in toStrip:
                newStr.remove(r)
                stripLen += 1
            str(stripLen)
            time.sleep(0.25)
            print("Instances of %s:%s"%(toStrip, stripLen)) #D
        #print("Final string:", newStr) #D
        for w in newStr:
            finalStr += w
        time.sleep(0.25)
        print("Collated form of '%s' is: '%s'"%(randStr, finalStr))
        time.sleep(0.3)
        print()
        # now that we have toStrip values, run for loop over randStr
        # deleting each toStrip value in randStr until toStrip can no longer be found
        # in what remains of randStr


stripRe(stuff)
stripRe(stuff, "o")
stripRe(stuff1, "03")
stripRe(stuff1, "1M")
stripRe(stuff2, "o")
stripRe(stuff3)


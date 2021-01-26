#digitalRoots.py
#produces the digital root of any positive integer
# where n contains [a, b] digits, its digital root DR(n) = a+b, provided a+b < 10
#the output cannot be greater than one digit in length

print("Enter a positive integer: ")
intValue = input()

def getRoot(number):
    numList = list(number)
    print("The integers that make up this number are: "+ str(numList[:]))
    potentialRoot = 0
    for n in numList:
        potentialRoot += int(n)
        #print(potentialRoot)
        global pRootCopy
        pRootCopy = potentialRoot #saves a copy of value stored in potentialRoot
    return potentialRoot

print(getRoot(intValue)) #potentialRoot is gone, but we have pRootCopy

while pRootCopy > 9: #repeat getRoot operation while the number is greater than two digits in length
    print(getRoot(str(pRootCopy)))
    continue
    if pRootCopy <= 9: #when only one digit remains, that value is the digital root
        break





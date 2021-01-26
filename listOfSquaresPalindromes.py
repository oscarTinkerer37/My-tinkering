#list of squared numbers for finding palindromes
#Created on windows pc

import time, pprint

#A list of numbers with lengths of two or more digits (10-899 default) along with their squared values will be printed out.
#The program will alert the user when a non-palindromic base produces a palindromic square.
      
print()
time.sleep(0.2)

bplusSquare = []
onlySquare = []
onlyBase = []

for b in range(10, 900): #List of numbers
    cuadr = b**2
    base = list(str(b))
    base2 = base.copy()
    base.reverse()

    sq = list(str(cuadr))
    cuadr2 = sq.copy()
    sq.reverse()

    print(b, cuadr)
    time.sleep(0.1)

    if base2 == base and sq == cuadr2:
        print('Base %s and squared %s are palindromes' %(b, cuadr))
        bplusSquare.append(base)
        bplusSquare.append(sq)
        time.sleep(0.1)
        
    if base2 != base and sq == cuadr2:
        print('Base %s non-palindrome... Square %s is a palindrome' %(b, cuadr))
        onlySquare.append(base2)
        onlySquare.append(sq)
        time.sleep(0.1)
        
    if base2 == base and sq != cuadr2:
        print('Base %s is a palindrome... square %s non-palindrome.' %(b, cuadr))
        onlyBase.append(base2)
        onlyBase.append(cuadr2)
        time.sleep(0.05)


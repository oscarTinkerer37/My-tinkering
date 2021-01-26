#lista de cuadrados para hallar palindromas

import time, winsound, pprint

winsound.Beep(400, 500)
#winsound.MB_ICONHAND #can't make it work...
print('Se imprimirá una lista de números de dos dígitos o más y sus cuadrados.\nEste programa indicará si alguna base no-palindrómica produce un cuadrado palindrómico.')
print()
time.sleep(0.2)

bplusSquare = []
onlySquare = []
onlyBase = []

for b in range(10, 900):
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
        print('Base %s y cuadrado %s palindrómicos' %(b, cuadr))
        #print()
        bplusSquare.append(base)
        bplusSquare.append(sq)
        winsound.Beep(320, 300) #Beep (Hertz, milisegundos)
        time.sleep(0.1)
        
    if base2 != base and sq == cuadr2:
        print('Base %s no-palindrómica... Cuadrado %s Palindrómico' %(b, cuadr))
        #print()
        onlySquare.append(base2)
        onlySquare.append(sq)
        winsound.Beep(750, 350) #Beep (Hertz, milisegundos)
        winsound.Beep(720, 310)
        winsound.Beep(650, 320)
        #winsound.MessageBeep(5) #-1 es el predeterminado
        time.sleep(0.1)
        
    if base2 == base and sq != cuadr2:
        print('Base %s palindrómica... cuadrado %s no-palindrómico.' %(b, cuadr))
        #print()
        onlyBase.append(base2)
        onlyBase.append(cuadr2)
        winsound.Beep(300, 250) #Beep (Hertz, milisegundos)
        time.sleep(0.05)

#polish this one
#pprint not usable with list type
#print('Base+Cuadrado: ', bplusSquare)
#print()
#print('Solo cuadrado: ', onlySquare)
#print()
#print('Solo base: ', onlyBase)

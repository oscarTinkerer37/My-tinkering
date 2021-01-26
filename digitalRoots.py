#digitalRoots.py
#obtiene la raíz digital de un entero positivo cualquiera
# donde n contiene [a, b] dígitos, su raíz digital DR(n) = a+b, siempre y cuando a+b < 10
#DR no puede ser más de un dígito

print("Ingrese número: ")
intValue = input()

def getRoot(number): #FUNCIONA!
    numList = list(number)
    print("Los enteros que componen a este número son: "+ str(numList[:]))
    potentialRoot = 0
    for n in numList:
        potentialRoot += int(n)
        #print(potentialRoot)
        global jiffy
        jiffy = potentialRoot #guarda el valor de potentialRoot
    return potentialRoot

print(getRoot(intValue)) #potentialRoot ya no existe, pero tenemos a jiffy de respaldo

while jiffy > 9: #mientras tenga más de dos dígitos, repetir operación getRoot
    print(getRoot(str(jiffy)))
    continue
    if jiffy <= 9: #cuando quede un solo dígito, esa es la raíz digital
        break

###def getMulti(number): #no funciona porque conceptualmente no están obteniendo múltiplos
"""    global multiples
    multiples = [] #lista de los múltiplos
    mIncr = int(number)*int(intValue)#múltiplo por valor
    multiples.append(mIncr)
    for x in range(1, 21):
        grow = int(multiples[0]) + mIncr
        multiples.append(grow)
    return multiples

print ("¿Desea obtener múltiplos base [n] de este número? [ENTER en caso contrario]")
mult = input()
if mult == '':
    print ("Ok")
elif mult != '':
    print (getMulti(mult))
"""




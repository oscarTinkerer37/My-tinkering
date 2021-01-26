#! python3

import time, os, winsound
#localDico = {'yr':0, 'mon':0, 'day':0, 'hour':0, 'min':0, 'sec':0, 'wday':0, 'yday':0, 'isdist':0}
localDico = {'yr':0, 'mon':0, 'day':0, 'hour':0, 'min':0}

directory = os.getcwd()
myDir = "C:\\MyPythonScripts"

if directory == myDir:
    print("Verificación de directorio - OK")
else:
    os.chdir("C:\\MyPythonScripts")
    print("Se ha cambiado a directorio C:\\MyPythonScripts") 
    #cambia a directorio con archivo py, bat y txt

localTimeList = list()
for t in time.localtime():
    localTimeList.append(t)
#print(localTimeList)#D

#n = 0
#for x in localDico.keys():
#    localDico[x] = localTimeList[n]
#    n += 1

#Los diccionarios no son iguales entre 3.5 y 3.8
#Asignando individualmente valores de diccionario
localDico['yr'] = localTimeList[0]
localDico['mon'] = localTimeList[1]
localDico['day'] = localTimeList[2]
localDico['hour'] = localTimeList[3]
localDico['min'] = localTimeList[4]

#print(localDico) #D
    #no pude usar bucles for anidados, entonces un solo for que recorre las llaves
    #del diccionario creado. Se iteran los índices de la lista mediante un enhanced assignment
    #adentro del for.

curr = str(localDico['yr']) + '.' + str(localDico['mon']) + '.' + str(localDico['day'])
timeEntered = str(localDico['hour']) + ":" + str(localDico['min'])  

time.sleep(0.3)
enter = input("Ingrese texto, el cual se registrará con fecha y hora: ")
time.sleep(0.4)
newLine = open("textlog.txt", "a")
newLine.write(enter + ' - ' + curr + ' @' + timeEntered +'h\n')
newLine.close()
time.sleep(0.4)

readLog = open("textlog.txt", "r")
print("Contenido de archivo a la fecha %s \n"%(curr))
for x in readLog.readlines():
    print(x)
    winsound.Beep(600, 450)
    time.sleep(0.3)

readLog.close()

time.sleep(2)


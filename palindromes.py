#palindrome finder
#RESUELTO (10/JUL/17)
#usé función list.reverse() en lugar de list.sort(reverse=True)
import time
print('Ingrese el número cuyas potencias (^2, ^3) desee verificar si son palindromas: ')

myNum = input()


square = int(myNum)**2
print(myNum + '^2 = ' +str(square))
chkSq = list(str(square))
chkSq.reverse()
if chkSq == list(str(square)):
    print('Palindroma: ' + str(square) + ' == ' + (str(''.join(chkSq))))
else:
    print(str(square) + ' NO es palindroma')
print()

time.sleep(0.25)

cube = int(myNum)**3
print(myNum + '^3 = ' +str(cube))
chkCube = list(str(cube))
chkCube.reverse()
if chkCube == list(str(cube)):
    print('Palindroma: ' + str(cube) + ' == '+ (str(''.join(chkCube))))
else:
    print(str(cube) + ' NO es palindroma')

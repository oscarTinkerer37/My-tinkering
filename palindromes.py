#palindrome finder
#used list.reverse() instead of list.sort(reverse=True)
import time
print('Enter the number whose squared and cubed values will be checked for palindromic quality: ')

myNum = input()


square = int(myNum)**2
print(myNum + '^2 = ' +str(square))
chkSq = list(str(square))
chkSq.reverse()
if chkSq == list(str(square)):
    print('Palindrome: ' + str(square) + ' == ' + (str(''.join(chkSq))))
else:
    print(str(square) + ' NOT a palindrome')
print()

time.sleep(0.25)

cube = int(myNum)**3
print(myNum + '^3 = ' +str(cube))
chkCube = list(str(cube))
chkCube.reverse()
if chkCube == list(str(cube)):
    print('Palindrome: ' + str(cube) + ' == '+ (str(''.join(chkCube))))
else:
    print(str(cube) + ' NOT a palindrome')

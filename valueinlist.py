print('Enter list of elements')
list=input()
newList=list.split(' ')
listInteger=[int(i) for i in newList]
print(' enter number to cheeck')
i=int(input())
if i in listInteger:
	print(f'{i} is in {listInteger}')
else:
	print(f'{i} is not in {listInteger}')

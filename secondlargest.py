print('Enter list of elements')
list=input()
newList=list.split(' ')
listInteger=[int(i) for i in newList]
listCopy=listInteger.copy()
if len(listCopy)<2:
	print('only one number is there')
elif len(listCopy)==2:
	if listCopy[0]==listCopy[1]:
		print('Both numbers are equal')
	else:
		index=listCopy.index(max(listCopy))
		listCopy.pop(index)
		print(f'second largest number {max(listCopy)}')
else:
	index=listCopy.index(max(listCopy))
	listCopy.pop(index)
	print(f'second largest number {max(listCopy)}')

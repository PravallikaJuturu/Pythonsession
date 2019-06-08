print('Enter list of elements')
list=input()
newList=list.split(' ')
myList=[int(i) for i in newList]
if myList[0]==myList[1] or myList[1]==myList[2] or myList[0]==myList[2]:
	print(0)
else:
	print(sum(myList))

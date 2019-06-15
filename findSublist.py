print('Enter first list')
list=input()
firstList=list.split(' ')
print('Enter second list')
list=input()
secondList=list.split(' ')
firstList.append(secondList)
print(firstList)
i=0
while i<len(firstList):
	if type(firstList[i])=='list':
		print('List has sublist')
	i+=1
else:
	print('list doesnot have sublist')
	
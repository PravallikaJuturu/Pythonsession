print('Enter list of elements')
list=input()
newList=list.split(' ')
listInteger=[int(i) for i in newList]
print('Smallest number in list is ',min(listInteger))
listInteger.sort()
print('Smallest number in list is ',listInteger[0])

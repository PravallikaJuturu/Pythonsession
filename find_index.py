print('Enter list of elements')
list=input()
newList=list.split(' ')
listInteger=[int(i) for i in newList]
print('My list is ',listInteger)
print('Enter number to  find index')
number=int(input())
print(f'{number} index in list is {listInteger.index(number)}')

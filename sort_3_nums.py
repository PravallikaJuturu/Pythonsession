myList=[54,13,74]
print('my List is ',myList)
minNum=min(myList)
maxNum=max(myList)
myList.remove(minNum)
myList.remove(maxNum)
print(f'sorted list {minNum} {myList[0]} {maxNum}')


my_List=input('Enter list items ')
my_List=my_List.split(',')
my_List=[int(i) for i in my_List]
removelist=[]
count=1
for i in my_List:
	
	if(count%3==0):
		count=count+1
		data=my_List[count-1]
		removelist.append(data)
print(removelist)
for j in removelist:
	my_List.remove(j)
print(my_List)
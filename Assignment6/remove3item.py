def remove_item(mylist):
	lenoflist=len(mylist)
	index=0
	pos=2
	while lenoflist>0:
		index=(index+pos)%lenoflist
		print(mylist.pop(index))
		lenoflist-=1
my_List=input('Enter list items ')
my_List=my_List.split(',')
my_List=[int(i) for i in my_List]
remove_item(my_List)
	
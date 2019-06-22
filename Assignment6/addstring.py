my_List=input('Enter list items ')
my_List=my_List.split(',')
my_List=[int(i) for i in my_List]
my_string=input('enter input string ')
output_list=[]
for i in my_List:
	output_list.append(my_string+str(i))
print(output_list)
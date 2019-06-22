my_dict={1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
print('My dictionary is ', my_dict)
key_list=list(my_dict.keys())
print(key_list)
print('enter key value to find')
key=int(input())
if key in key_list:
	print(f'{key} is there in my_dict keys list')
else:
	print(f'{key} is not there in my_dict keys list')
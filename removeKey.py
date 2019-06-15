my_dict={1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
print('My dictionary is ', my_dict)
key_list=list(my_dict.keys())
value_list=list(my_dict.values())

print(f'Max value in dictionary is {max(value_list)}')

print(f'Min value in dictionary is {min(value_list)}')

print('Enter key to remove from dictionary')
key=int(input())
if key in key_list:
	my_dict.pop(key)
	print(my_dict)
else:
	print('key is not there in list')
	
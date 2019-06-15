my_dict={1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
print('My dictionary is ', my_dict)
value_list=list(my_dict.values())
value_list.sort()
print(f'Highest 3 values are {value_list[-3:]}')
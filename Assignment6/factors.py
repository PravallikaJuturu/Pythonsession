number=int(input('Enter number '))
result_list=[]
for i in range(1,number+1):
	if number%i==0 and i<number+1:
		result_list.append(i)
	else:
		pass
print(result_list)
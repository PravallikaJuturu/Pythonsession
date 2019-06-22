number=int(input('Enter number '))
result_list=[]
for i in range(1,number+1):
	if number%i==0 and i<number+1:
		result_list.append(i)
	else:
		pass
if result_list==[1,number]:
	print(f'{number} is prime number')
else:
	print(f'{number} is not prime number')
	
		
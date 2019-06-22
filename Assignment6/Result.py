final_list=[]
for mynumber in range(100,401):
	number=mynumber
	while number>0:
		number=number%10
		if number%2!=0:
			break
		else:
			number=int(number/10)
			
			
			final_list.append(mynumber)
print(final_list)
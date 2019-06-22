result_list=[]
count=0
for i in range(100,401):
	for num in str(i):
		if int(num)%2!=0:
			break
		else:
			count+=1
	if count== len(str(i)):
		result_list.append(str(i))
	count = 0
print(",".join(result_list))

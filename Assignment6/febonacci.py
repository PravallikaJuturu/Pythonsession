number=int(input('Enter number'))
first_index=0
second_index=1
febonacci_series=[0,1]
for i in range(number):
	next_num=febonacci_series[first_index]+febonacci_series[second_index]
	febonacci_series.append(next_num)
	first_index+=1
	second_index+=1
print(febonacci_series)
	
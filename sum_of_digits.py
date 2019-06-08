print('Enter number')
myNumber=int(input())
sumOfdigits=0
while myNumber>0:
	digit=myNumber%10
	sumOfdigits=sumOfdigits+digit
	myNumber=int(myNumber/10)
print(f'Sum of digits = {sumOfdigits}')

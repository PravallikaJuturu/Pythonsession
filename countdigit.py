print('Enter string')
user_string=input()
countofDigits=0
countofLetters=0
for i in user_string:
	if i.isdigit():
		countofDigits+=1
	else:
		countofLetters+=1
	
print(f'In {user_string}, {countofDigits} digits and {countofLetters} letters are there')	
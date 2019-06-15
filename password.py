print('Enter Password: ')
password=input()
smallletters="abcdefghijklmnopqrstuvwxyz"
capitalletters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
specialchars="$#@"
A=0
B=0
C=0
D=0
for i in password:
	if i in smallletters:
		A += 1
	if i in capitalletters:
		B+=1
	if i in numbers:
		C+=1
	if i in specialchars:
		D+=1

if len(password)>6 and len(password)<16:
	if A==0:
		print('Must have atlease 1 character from (a-z)')
	if B==0:
		print('Must have atlease 1 character from (A-Z)')
	if C==0:
		print('Must have atlease 1 character from (1-9)')
	if D==0:
		print('Must have atlease 1 character from ($#@)')

else:
	print('Password lenth must be 6 to 16 characters')
print('Enter IP Address')
ipAddress=input()
ipAddress_list=ipAddress.split('.')
if len(ipAddress_list)==4:
	if len(ipAddress_list[0])==3 and len(ipAddress_list[1])==3:
		if len(ipAddress_list[2])!=2 and len(ipAddress_list[3])!=2:
			print('IP Address is not valid')
		else:
			print('IP Adress is valid')
	else:
		print('IP Address is not valid')
else:
	print('IP Address is not valid')
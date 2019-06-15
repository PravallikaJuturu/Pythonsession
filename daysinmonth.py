print('List of months: January, February, March, April, May, June, July, August, September, October, November, December')
print('Enter the name of month')
monthName=input()
if monthName.upper()=='FEBRUARY':
	print('No of Days: 28/29 days')
elif monthName in ('January','March','May','July','August','October','December'):
	print('No of Days: 31 days')
elif monthName in ('April','June','September','November'):
	print('No of Days: 30 days')
else:
	print('Invalid month')
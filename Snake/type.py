#input

my_numbers =[23,11,1992]
integer = "the aray you entered is of integer type"
sum = 0
for i in my_numbers:
	sum+= i 
print integer
print sum


my_string = ['Atssini','Cabrera']
integer = "The array you entered is of string type"
print integer
for name in my_string:
	print name

full_list= [23,'Atssini', 11, 'Cabrera',1992]
def typelisting():
	arr = []
	newstr = ''
	for i in full_list:
		if type(i)==float or type(i)==int:
			arr.append(i)
			numsum = sum(list(arr))
		elif type(i)==str:
			newstr += '' + i
print('Str:', newstr)
print('Sum:', numsum)


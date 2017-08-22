#find charaters
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list =[]

for item in word_list:
	if (item.find(char) >0):
		new_list.append(item)
print new_list




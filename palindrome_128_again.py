string=input()
list=[]
for i in range(0,len(string)):
	for j in range(i+1,len(string)):
		new=string[i:j+1]
		new_1=new[::-1]
		if new==new_1:
			list.append(new)
for i in list:
	print(i)

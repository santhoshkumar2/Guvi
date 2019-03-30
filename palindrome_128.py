string=input()
list=[]
list_2=[]
for i in range(0,len(string)):
	for j in range(i+1,len(string)):
		new=string[i:j+1]
		new_1=new[::-1]
		if new==new_1:
			list.append(new)
for i in list:
	if(len(i)>1):
		list_2.append(i)
list_2.sort(key=len)
for i in list_2:
	print(i)

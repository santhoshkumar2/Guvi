a=raw_input()
a=a.split()
for num in range (int(a[0]),int(a[1])+1):
	if(num>1):
		for i in range (2,num):
			if(num%i)==0:
				break
		else:
			a=len([num])
			print a
		

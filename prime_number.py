num=int(input())
a=[]
for i in range(2,num):
	for j in range(2,i+1):
		if i%j==0:
			break
	if i==j and i%10==3:
		a.append(i)
print(sum(a))

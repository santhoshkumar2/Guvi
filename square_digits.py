num=int(input())
num_1=0
while(num!=0):
	a=num%10
	num_1=num_1+a*a
	num//=10
print (num_1)

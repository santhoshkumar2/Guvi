a=raw_input()
b=raw_input()
a=a.split()
b=b.split()
sum=0
for i in range(int(a[1])):
	sum=sum+int(b[i])
print sum

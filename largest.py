a1=int(raw_input())
b1=int(raw_input())
c1=int(raw_input())
if (a1>=b1) and (a1>=c1):
	largest=a1
elif (b1>=a1) and (b1>=c1):
	largest=b1
else:
	largest=c1
print int(largest)

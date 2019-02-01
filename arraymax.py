num=int(raw_input())
arr=raw_input()
arr=arr.split()
max=int(arr[0])
for i in range(1,num):
	if int(arr[i])>max:
		max=int(arr[i])
print max

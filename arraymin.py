num=int(raw_input())
arr=raw_input()
arr=arr.split()
min=int(arr[0])
for i in range(1,num):
	if int(arr[i])<min:
		min=int(arr[i])
print min

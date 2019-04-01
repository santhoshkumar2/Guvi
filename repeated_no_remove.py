num=int(input())
num_1=input().split()
dict={}
list=[]
for i in num_1:
	dict[i]=num_1.count(i)
	if(dict[i]==1):
		list.append(i)
print(*list)

num=input()
list=input().split()
new=max(set(list), key = list.count)
print(new)

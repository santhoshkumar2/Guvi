num1,num2=map(int,input().split())
arr=input().split()
new_arr=(arr[-num2:]+arr[:-num2])
print(*new_arr)

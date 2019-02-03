a=int(raw_input())
b=int(raw_input())
for num in range(a,b):
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum =sum+digit ** 3
       temp=temp//10
 
   if num == sum:
       print num

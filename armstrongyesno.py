usr=raw_input()
usr=int(usr)
sum=0
temp=usr
while usr>0:
    rem=usr%10
    sum=sum+(rem**3)
    usr=usr/10
if sum==temp:
    print"yes"
else:
    print'no'

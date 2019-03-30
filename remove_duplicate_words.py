string=input()
for i in range(len(string)):
    if(string.count(string[i])==1):
        print(string[i],end="")

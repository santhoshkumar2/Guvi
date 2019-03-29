num=int(input())
for i in range(0, num):
    for j in range(num, i, -1):
        print("1 ", end="")
    print("\r")

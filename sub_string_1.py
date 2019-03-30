word_1,word_2=map(str,(input()).split())
new=[]
if(word_2 in word_1):
    print(word_2)
else:
    for i in range(0,len(word_2)):
        for j in range(0,len(word_2)):
            if(word_1[i]==word_2[j]):
                new.append(word_1[i])            
print("".join(new))

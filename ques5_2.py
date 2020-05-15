count1=0
count2=0
for i in range(1 , 100):
    sq=i**2
    if sq%10 == 4:
        count1=count1+1
    if sq==9:
        count2=count2+1    
print(count1 , "squares are ends with 4 ")
print(count2 , "squares are ends with 9")
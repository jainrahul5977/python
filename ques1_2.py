#Print a box like the one below
for i in range(4):
    if i==1 or i==2:
        for j in range(19):
            if j==0 or j==18:
                print("*" , end =" ")
            else :
                print(end = "  ")
    else : 
        for j in range(19):
            print("*" , end = " ")
    print()
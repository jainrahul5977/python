#Ask the user to enter a number x . Use the sep optional argument to print out x , 2x , 3x , 4x ,
#and 5x , each separated by three dashes, like below.
#Enter a number: 7
#7---14---21---28---35
i= int(input("enter the number: "))
for j in range(1,6,1):
    print(j*i,"-" , sep = "--" , end="")
#Ask the user to enter a number. Print out the square of the number, but use the sep optional
#argument to print it out in a full sentence that ends in a period. Sample output is shown
#below.56
#Enter a number: 5
#The square of 5 is 25.
i = int(input("enter a number: "))
print("the square of",i ,"is", i*i , sep = " ")
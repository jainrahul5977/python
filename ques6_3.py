str = input("insert any formula : ")
left_para = str.count("(")
right_para = str.count(")")
if left_para == right_para :
    print(" the given formula is correct")
else :
    print("formula is wrong")
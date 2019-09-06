m=int(input("enter marks in maths"))
p=int(input("enter marks in physics"))
c=int(input("enter marks in chemistry"))
if m>100 or p>100 or c>100:
    print("not valid marks")
elif (m<35 or p<35 or c<35):
    print("fail")
elif m>=35 and p>=35 and c>=35:
    print("pass")
    sum=(m+p+c)/3
    print("average",sum)
    if (sum<=59):
        print("your grade is C")
    elif (sum<=69): 
        print("your grade is B")
    else:
        print("your grade is A")

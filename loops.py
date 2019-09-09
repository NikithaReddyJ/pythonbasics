a=int(input("enter a number"))
x=0
while x<a:
    x=x+1
    if x==100:
        break
    elif x%10==0:
        continue
    else:
        print(x)

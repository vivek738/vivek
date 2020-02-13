def add(a,b):
    z=a+b
    return z
def substraction(a,b):
    z=a-b
    return z
def multiplication(a,b):
    z=a*b
    return z
def divide(a,b):
    z=a/b
    return z
x=int(input("1.add 2.substraction 3.multiplication 4.division "))
a = int(input("enter a number: "))
b = int(input("enter a number: "))
if x==1:
    ans =add(a,b)
    print (ans)
elif x==2:
    ans=substraction(a,b)
    print (ans)
elif x==3:
   ans=multiplication(a,b)
   print(ans)
elif x==4:
    ans=divide(a,b)
    print(ans)
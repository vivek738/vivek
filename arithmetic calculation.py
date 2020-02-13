def add():
    a=int(input("enter a number: "))
    b=int(input("enter a number: "))
    c=a+b
    print("sum is",c)
def substraction():
    a=int(input("enter a number: "))
    b=int(input("enter a number: "))
    c=a-b
    print("substraction is",c)
def multiplication():
    a=int(input("enter a number: "))
    b=int(input("enter a number: "))
    c=a*b
    print("multiplication is",c)
def divide():
    a=int(input("enter a number: "))
    b=int(input("enter a number: "))
    c=a/b
    print("division is",c)
x=int(input("1.add,2.substraction,3.multiplication 4.division "))
if x==1:
    add()
elif x==2:
    substraction()
elif x==3):
   multiplication()
elif x==4:
    divide()
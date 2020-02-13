try:
    x=int(input("enter first no."))
    y=int(input("enter second no."))
    c=x/y
    print(c)
except ZeroDivisionError:
    print("you have enter 0 in y, which is not legal")
    print("please re enter value for y ")
    y=int(input())
    print(x/y)
except ValueError:
    print("you have enter string instead of no.")
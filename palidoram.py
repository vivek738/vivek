a=int(input("enter a number"))
b=a
rev=0
while(a>0):
    digit=a%10
    rev=rev*10+digit
    a=a//10
if rev==b:
    print ("palindrome")
else:
    print("not palindrome")


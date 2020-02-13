x=int(input("enter a number"))
def function(x):
    sum=0
    while x>0:
        d=x%10
        sum=sum+d
        x=x//10
    return(sum)
ans=function(x)
print(ans)
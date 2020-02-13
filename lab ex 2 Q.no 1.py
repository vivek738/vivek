sub1 =int(input("enter marks of the first subject: "))
sub2 =int(input("enter mark of the second subject: "))
sub3 =int(input("enter mark of the third subject: "))
sub4 =int(input("enter mark of the third subject: "))
avg=(sub1+sub2+sub3+sub4)/4
if (avg>=70) and (avg<=100):
    print("grade:distinction")
elif(avg>=60) and (avg<=100):
    print("grade:first devision")
elif(avg>=40) and (avg<=100):
    print("grade:pass")
elif(avg>=40) and (avg<=100):
    print("grade:fail")
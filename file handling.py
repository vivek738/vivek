f=open("a.jpg","rb")
temp=f.read()
f1=open('abc.txt','wb')
f1.write(temp)
f1.close()
f.close()




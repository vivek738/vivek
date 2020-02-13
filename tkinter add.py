from tkinter import*
wn=Tk()
wn.title("GUI_form")
def abc():

wn.geometry('600x400')
a=Label(wn,text="first num")
a.grid()
b=Label(wn,text="second num")
b.grid()
c=Button(wn,text="add",abc)
c.grid(row=2,column=1)

#def abc(e):
   # num_1=int(input("enter a number "))
   # num_2=int(input("enter a number"))
bentry=Entry(wn)
bentry.grid(row=1,column=1)


aentry=Entry(wn)
aentry.grid(row=0,column=1)

#btn_1.bind('<Button_1>'abc)






wn.mainloop()

from tkinter import *
rt2=Tk()
rt2.title("Vending Machine")
rt2.geometry("500x750")
Label(rt2,text="Vending Machine",font=("bold",19),width=25).place(x=15,y=10)
Label(rt2,text="Choose your item :",font=(20)).place(x=50,y=118)
v=IntVar()
a=Radiobutton(rt2,text="French Fries = 80Rs",value=1,variable=v).place(x=60,y=150)
b=Radiobutton(rt2,text="Softy = 30Rs",value=2,variable=v).place(x=60,y=200)
c=Radiobutton(rt2,text="Cup Cake = 20Rs",value=3,variable=v).place(x=60,y=250)
d=Radiobutton(rt2,text="Dora Cake = 30Rs",value=4,variable=v).place(x=60,y=300)
e=Radiobutton(rt2,text="Cold Coffee = 30Rs",value=5,variable=v).place(x=60,y=350)
f=Radiobutton(rt2,text="Hot Coffee = 40Rs",value=6,variable=v).place(x=60,y=400)
g=Radiobutton(rt2,text="Green Tea =30Rs",value=7,variable=v).place(x=60,y=450)
h=Radiobutton(rt2,text="Tea = 20Rs",value=8,variable=v).place(x=250,y=150)
i=Radiobutton(rt2,text="Ice Tea = 30Rs",value=9,variable=v).place(x=250,y=200)
j=Radiobutton(rt2,text="Coca Cola = 40Rs",value=10,variable=v).place(x=250,y=250)
k=Radiobutton(rt2,text="Pepsi = 40Rs",value=11,variable=v).place(x=250,y=300)
l=Radiobutton(rt2,text="Mirinda = 40Rs",value=12,variable=v).place(x=250,y=350)
m=Radiobutton(rt2,text="Lays = 20Rs",value=13,variable=v).place(x=250,y=400)
n=Radiobutton(rt2,text="Kurkure = 20Rs",value=14,variable=v).place(x=250,y=450)
Label(rt2,text="Enter Your Cash :",font=(20)).place(x=10,y=500)
Label(rt2,text="Your Cashback :",font=(20)).place(x=10,y=550)
s=IntVar()
o=Entry(rt2,textvariable=s).place(x=200,y=500)

s1=IntVar()
p=Entry(rt2,textvariable=s1).place(x=200,y=550)
def cancel1():
    rt2.destroy()

def clicked():
    i=s.get()
    selection=v.get()
    if(selection==1 and i>=80):
        i=i-80
        s1.set(i)
    elif(selection==2 and i>=30):
        i=i-30
        s1.set(i)
    elif(selection==3 and i>=20):
        i=i-20
        s1.set(i)
    elif(selection==4 and i>=30):
        i=i-30
        s1.set(i)
    elif(selection==5 and i>=30):
        i=i-30
        s1.set(i)
    elif(selection==6 and i>=40):
        i=i-40
        s1.set(i)
    elif(selection==7 and i>=30):
        i=i-30
        s1.set(i)
    elif(selection==8 and i>=30):
        i=i-30
        s1.set(i)
    elif(selection==9 and i>=40):
        i=i-40
        s1.set(i)
    elif(selection==10 and i>=40):
        i=i-40
        s1.set(i)
    elif(selection==11 and i>=40):
        i=i-40
        s1.set(i)
    elif(selection==12 and i>=40):
        i=i-40
        s1.set(i)
    elif(selection==13 and i>=20):
        i=i-20
        s1.set(i)
    elif(selection==14 and i>=20):
        i=i-20
        s1.set(i)
    else:
        rt3=Tk()
        rt3.title("Error")
        rt3.geometry("300x100")
        Label(rt3,text="Insufficient Amount!!",font=(19)).place(x=15,y=10)
        def cancel():
            rt3.destroy()
        Button(rt3,text="OK",bg="black",fg="white",command=cancel).place(x=75,y=50)
#def clear():
 #   v.delete(0,'end')
  #  s.delete(0,'end')
   # s1.delete(0,'end')
        
Button(rt2,text="Submit",bg="black",fg="white",command=clicked).place(x=300,y=650)
Button(rt2,text="Cancel",bg="black",fg="white",command=cancel1).place(x=350,y=650)
#Button(rt2,text="Clear",bg="black",fg="white",command=clicked).place(x=400,y=650)

rt2.mainloop()

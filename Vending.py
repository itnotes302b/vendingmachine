from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmg
rt2 = Tk()
rt2.title("Vending Machine")
rt2.geometry("700x750")
Label(rt2, text="Vending Machine", fg="red",font="cosmicsansms 20 bold").place(x=250,y=20)
Label(rt2, text="Choose your item :", font=(20)).place(x=50, y=118)
v = IntVar() #for radio button
db_a = IntVar()
db_b = IntVar()
db_c = IntVar()
db_d = IntVar()
db_e = IntVar()
db_f = IntVar()
db_g = IntVar()
db_h = IntVar()
db_i = IntVar()
db_j = IntVar()
db_k = IntVar()
db_l = IntVar()
db_m = IntVar()
db_n = IntVar()

a = Radiobutton(rt2, text="French Fries = 80Rs", value=1, variable=v).place(x=60, y=150)
a_db = ttk.Combobox(rt2,width=5,textvariable=db_a)
a_db['values']=(1,2,3,4,5,6,7,8,9,10)
a_db.place(x =250 ,y =150)
a_db.current(0)

b = Radiobutton(rt2, text="Softy = 30Rs", value=2, variable=v).place(x=60, y=200)
b_db = ttk.Combobox(rt2,width=5,textvariable=db_b)
b_db['values']=(1,2,3,4,5,6,7,8,9,10)
b_db.place(x =250 ,y =200)
b_db.current(0)


c = Radiobutton(rt2, text="Cup Cake = 20Rs", value=3, variable=v).place(x=60, y=250)
c_db = ttk.Combobox(rt2,width=5,textvariable=db_c)
c_db['values']= (1,2,3,4,5,6,7,8,9,10)
c_db.place(x =250 ,y =250)
c_db.current(0)

d = Radiobutton(rt2, text="Dora Cake = 30Rs", value=4, variable=v).place(x=60, y=300)
d_db = ttk.Combobox(rt2,width=5,textvariable=db_d)
d_db['values']= (1,2,3,4,5,6,7,8,9,10)
d_db.place(x =250 ,y =300)
d_db.current(0)

e = Radiobutton(rt2, text="Cold Coffee = 30Rs", value=5, variable=v).place(x=60, y=350)
e_db = ttk.Combobox(rt2,width=5,textvariable=db_e)
e_db['values']= (1,2,3,4,5,6,7,8,9,10)
e_db.place(x =250 ,y =350)
e_db.current(0)

f = Radiobutton(rt2, text="Hot Coffee = 40Rs", value=6, variable=v).place(x=60, y=400)
f_db = ttk.Combobox(rt2,width=5,textvariable=db_f)
f_db['values']= (1,2,3,4,5,6,7,8,9,10)
f_db.place(x =250 ,y =400)
f_db.current(0)

g = Radiobutton(rt2, text="Green Tea =30Rs", value=7, variable=v).place(x=60, y=450)
g_db = ttk.Combobox(rt2,width=5,textvariable=db_g)
g_db['values']= (1,2,3,4,5,6,7,8,9,10)
g_db.place(x =250 ,y =450)
g_db.current(0)


h = Radiobutton(rt2, text="Tea = 20Rs", value=8, variable=v).place(x=350, y=150)
h_db = ttk.Combobox(rt2,width=5,textvariable=db_h)
h_db['values']= (1,2,3,4,5,6,7,8,9,10)
h_db.place(x =500 ,y =150)
h_db.current(0)



i = Radiobutton(rt2, text="Ice Tea = 30Rs", value=9, variable=v).place(x=350, y=200)
i_db = ttk.Combobox(rt2,width=5,textvariable=db_i)
i_db['values']= (1,2,3,4,5,6,7,8,9,10)
i_db.place(x =500 ,y =200)
i_db.current(0)



j = Radiobutton(rt2, text="Coca Cola = 40Rs", value=10, variable=v).place(x=350, y=250)
j_db = ttk.Combobox(rt2,width=5,textvariable=db_j)
j_db['values']= (1,2,3,4,5,6,7,8,9,10)
j_db.place(x =500 ,y =250)
j_db.current(0)



k = Radiobutton(rt2, text="Pepsi = 40Rs", value=11, variable=v).place(x=350, y=300)
k_db = ttk.Combobox(rt2,width=5,textvariable=db_k)
k_db['values']= (1,2,3,4,5,6,7,8,9,10)
k_db.place(x =500 ,y =300)
k_db.current(0)



l = Radiobutton(rt2, text="Mirinda = 40Rs", value=12, variable=v).place(x=350, y=350)
l_db = ttk.Combobox(rt2,width=5,textvariable=db_l)
l_db['values']= (1,2,3,4,5,6,7,8,9,10)
l_db.place(x =500 ,y =350)
l_db.current(0)

m = Radiobutton(rt2, text="Lays = 20Rs", value=13, variable=v).place(x=350, y=400)
m_db = ttk.Combobox(rt2,width=5,textvariable=db_m)
m_db['values']= (1,2,3,4,5,6,7,8,9,10)
m_db.place(x =500 ,y =400)
m_db.current(0)


n = Radiobutton(rt2, text="Kurkure = 20Rs", value=14, variable=v).place(x=350, y=450)
n_db = ttk.Combobox(rt2,width=5,textvariable=db_n)
n_db['values']= (1,2,3,4,5,6,7,8,9,10)
n_db.place(x =500 ,y =450)
n_db.current(0)





Label(rt2, text="Enter Your Cash :", font=(20)).place(x=10, y=500)
Label(rt2, text="Total Bill :", font=(20)).place(x=10, y=550)
Label(rt2, text="Your Cashback :", font=(20)).place(x=10, y=600)
s = IntVar()
o = Entry(rt2, textvariable=s).place(x=200, y=500)

t = IntVar()
t1= Entry(rt2, textvariable=t).place(x=200, y=550)

s1 = IntVar()
p = Entry(rt2, textvariable=s1).place(x=200 , y=600)


def cancel1():
    rt2.destroy()


def clicked():

    i = s.get()
    selection = v.get()

    if (selection ==1 ):
        qantity = db_a.get()
        total = qantity * 80
        t.set(total)
        if i > total:
            i=i-total
            s1.set(i)


    elif (selection == 2 and i >= 30):
        qantity = db_b.get()
        total = qantity * 30
        t.set(total)
        if i > total:
            i=i-total
            s1.set(i)

    elif (selection == 3 and i >= 20):
        qantity = db_c.get()
        total = qantity * 20
        t.set(total)
        if i > total:
            i=i-total
            s1.set(i)

    elif (selection == 4 and i >= 30):
        qantity = db_d.get()
        total = qantity * 30
        t.set(total)
        if i > total:
            i=i-total
            s1.set(i)

    elif (selection == 5 and i >= 30):
        qantity = db_e.get()
        total = qantity * 30
        t.set(total)
        if i > total:
            i=i-total
            s1.set(i)

    elif (selection == 6 and i >= 40):
        qantity = db_f.get()
        total = qantity * 40
        t.set(total)
        if i > total:
            i=i-total
            s1.set(i)

    elif (selection == 7 and i >= 30):
        qantity = db_g.get()
        total = qantity * 30
        t.set(total)
        if i > total:
            i=i-total
            s1.set(i)

    elif (selection == 8 and i >= 30):
        qantity = db_h.get()
        total = qantity * 80
        t.set(total)
        if i > total:
            i=i-total
            s1.set(i)

    elif (selection == 9 and i >= 40):
        qantity = db_i.get()
        total = qantity * 80
        t.set(total)
        if i > total:
            i=i-total

    elif (selection == 10 and i >= 40):
        qantity = db_j.get()
        total = qantity * 80
        t.set(total)
        if i > total:
            i=i-total
            s1.set(i)

    elif (selection == 11 and i >= 40):
        qantity = db_k.get()
        total = qantity * 80
        t.set(total)
        if i > total:
            i=i-total
            s1.set(i)
        else:
            tmg.askokcancel('ERROR',"$$$ Imsufficient amount $$$ ")
    elif (selection == 12 and i >= 40):
        qantity = db_l.get()
        total = qantity * 80
        t.set(total)
        if i > total:
            i=i-total
            s1.set(i)
        else:
            tmg.askokcancel('ERROR',"$$$ Imsufficient amount $$$ ")
    elif (selection == 13 and i >= 20):
        qantity = db_m.get()
        total = qantity * 80
        t.set(total)
        if i > total:
            i=i-total
            s1.set(i)
        else:
            tmg.askokcancel('ERROR',"$$$ Imsufficient amount $$$ ")
    elif (selection == 14 and i >= 20):
        qantity = db_n.get()
        total = qantity * 80
        t.set(total)
        if i > total:
            i=i-total
            s1.set(i)

    else:
        tmg.askokcancel('ERROR', "$$$ Imsufficient amount $$$ ")



Button(rt2, text="Submit", bg="black", fg="white", command=clicked).place(x=300, y=650)
Button(rt2, text="Cancel", bg="black", fg="white", command=cancel1).place(x=450, y=650)

rt2.mainloop()

from tkinter import  *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('Diary')
GUI.geometry('700x700')

L1 = Label(GUI,text='The record of income and expenses',font=('Angsana New',25),fg='blue')
L1.place(x=200,y=40)

######################

def Button1():
    text = '10000'
    messagebox.showinfo('Salary',text)
    
FB1 = LabelFrame(GUI)
FB1.place(x=100,y=100)
B1 = ttk.Button(FB1,text='income',command=Button1)
B1.pack(ipadx=30,ipady=30)

######################

def Button2():
    text = '5000'
    messagebox.showinfo('Car loan',text)
    
FB2 = LabelFrame(GUI)
FB2.place(x=500,y=700)
B2 = ttk.Button(FB1,text='Expenses',command=Button2)
B2.pack(ipadx=30,ipady=30)

######################
def Button3():
    text = '5000'
    messagebox.showinfo('Remind',text)

FB3 = LabelFrame(GUI)
FB3.place(x=500,y=500)
B3 = ttk.Button(FB1,text='Blance',command=Button3)
B3.pack(ipadx=30,ipady=30)

GUI.mainloop()

    

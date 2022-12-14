from tkinter import *
from tkinter import ttk


text = " soms"
text2 = " in KGZ soms"

converter = Tk()
converter.title("Unit Converter")
converter.geometry("600x400")

OPTIONS = {
    "British Pound":105.05,
    "Euro":90.36,
    "USD":84.95,
    "RUS Ruble": 1.34 
        }

def ok():
    price = soms.get()
    answer = variable1.get()
    DICT = OPTIONS.get(answer,None)
    converted = float(DICT)*float(price)
    result.delete(1.0,END)
    result.insert(INSERT,"Price of ",INSERT,answer,INSERT, text2, INSERT," = ",INSERT,converted, INSERT, text)
appName = Label(converter,text="Currency Converter",font=("arial",15,"bold","underline"),fg="dark green")
appName.place(x=200, y=10)

result = Text(converter, height=4,width=50,font=("arial",10,"bold"),bd=5)
result.place(x=125, y=60)

text1 = Label(converter,text="Value in selected currency:  " ,font=("arial",10,"bold"),fg="black")
text1.place(x=22, y=165)

soms = Entry(converter,font=("arial",20))
soms.place(x=200, y=160)

choice = Label(converter,text="Choice:",font=("arial",10,"bold"),fg="blue")
choice.place(x=30, y=220)

variable1 = StringVar(converter)
variable1.set(None)
option = OptionMenu(converter,variable1,*OPTIONS)
option.place(x=100 , y=210,width=100, height=40)

button = Button(converter,text="Convert",fg="RoyalBlue1",font=("arial",20),bg="azure2",command=ok)
button.place(x=200, y=210,height=35,width=150)


converter.mainloop()
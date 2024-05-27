from tkinter import *

window = Tk()
window.title("tk")
window.geometry('296x292')
window.resizable(0, 0)
window.configure(bg="#EEEEEE")
def calculate(operation):
    try:
        value1=float(value1_entry.get())
        value2=float(value2_entry.get())
        if operation=='+':
            return result.set(value1+value2)
        elif operation == '-':
            result.set(value1 - value2)
        elif operation == '*':
            result.set(value1 * value2)
        elif operation == '/':
            result.set(value1 / value2 if value2 != 0 else 'Error')
    except ValueError:
        result.set('Invalid Input')


title_label = Label(window, text="Calculator", font=('', 14))
title_label.grid(row=0, column=0, padx=100, pady=20, columnspan=4,sticky="w")

value1_label = Label(window, text="Type Value 1:",font=("",10))
value1_label.grid(row=1, column=0,padx=52,pady=1,columnspan=2,sticky="w")
value1_entry = Entry(window, width=19)
value1_entry.grid(row=1, column=0, padx=142, pady=15,sticky="w")

value2_label = Label(window, text="Type Value 2:",font=("",10))
value2_label.grid(row=2, column=0,padx=52,pady=5,columnspan=2, sticky="w")
value2_entry = Entry(window, width=19)
value2_entry.grid(row=2, column=0, padx=142, pady=15,sticky="w")

button1 = Button(window, text="+", bg="green", fg="white", width=5,command=lambda:calculate("+"))
button1.grid(row=3, column=0, padx=62, pady=5,sticky="w",columnspan=4)
button2 = Button(window, text="-", bg="green", fg="white", width=5,command=lambda:calculate("-"))
button2.grid(row=3, column=0, padx=112, pady=5,columnspan=4,sticky="w")
button3 = Button(window, text="x", bg="green", fg="white", width=5,command=lambda:calculate("*"))
button3.grid(row=3, column=0, padx=162, pady=5,columnspan=4,sticky="w")
button4 = Button(window, text="/", bg="green", fg="white", width=5,command=lambda:calculate("/"))
button4.grid(row=3, column=0, padx=212, pady=5,columnspan=4, sticky="w")

result_label = Label(window, text="Result:",font=("",10))
result_label.grid(row=4, column=0,padx=70,pady=15,sticky="w")
result = StringVar()
result_entry = Entry(window, textvariable=result, state='readonly', width=20)
result_entry.grid(row=4, column=0, padx=140, pady=15,sticky="w")

window.mainloop()

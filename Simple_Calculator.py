import tkinter
from tkinter import messagebox

def submit_button_click():
    num1 = entry1.get()
    op = entry2.get()
    num2 = entry3.get()
    if num1 and op and num2:
        if op=="+" :
            sum=float(num1)+float(num2)
            response=f"sum={sum}"
        elif op=="-":
            sub=float(num1)-float(num2)
            response=f"Sub={sub}"
        elif op=="*" :
            mul = float(num1) * float(num2)
            response = f"Product={mul}"
        elif op=="%" :
            rem=float(num1)%float(num2)
            response=f"Remainder={rem}"
        elif op=="/" :
            quo=float(num1)/float(num2)
            response=f"Quoient={quo:.3f}"
        messagebox.showinfo("Output", response)
    else:
        messagebox.showerror("Error", "Please fill in all three inputs!")

obj = tkinter.Tk()
obj.title("Simple Calculator")

label1 = tkinter.Label(obj, text="Number 1:")
entry1 = tkinter.Entry(obj)

label2 = tkinter.Label(obj, text="Operator(+,-,*,/,%) :")
entry2 = tkinter.Entry(obj)

label3 = tkinter.Label(obj, text="Number 2:")
entry3 = tkinter.Entry(obj)

submit_button = tkinter.Button(obj, text="Calculate", command=submit_button_click)

label1.grid(row=0, column=0, padx=10, pady=10)
entry1.grid(row=0, column=1, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)
label3.grid(row=2, column=0, padx=10, pady=10)
entry3.grid(row=2, column=1, padx=10, pady=10)
submit_button.grid(row=3, columnspan=2, padx=10, pady=20)

obj.mainloop()


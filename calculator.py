import tkinter as tk

root = tk.Tk()
colour = 'cyan'
root.configure(background=colour, width=300)


def convertstr(s):
    """Convert string to either int or float."""
    try:
        result = int(s)
    except ValueError:
        result = float(s)
    return result


def add():
    result_box.delete('1.0', tk.END)
    a = first_number.get()
    b = second_number.get()
    if a and b:
        result = convertstr(a)+convertstr(b)
    else:
        result = "insert both numbers"
    result_box.insert(tk.INSERT, result)
    first_number.set('')
    second_number.set('')


def substract():
    result_box.delete('1.0', tk.END)
    a = first_number.get()
    b = second_number.get()
    if a and b:
        result = convertstr(a)-convertstr(b)
    else:
        result = "insert both numbers"
    result_box.insert(tk.INSERT, result)
    first_number.set('')
    second_number.set('')


def multiply():
    result_box.delete('1.0', tk.END)
    a = first_number.get()
    b = second_number.get()
    if a and b:
        result = convertstr(a)*convertstr(b)
    else:
        result = "insert both numbers"
    result_box.insert(tk.INSERT, result)
    first_number.set('')
    second_number.set('')


def divide():
    result_box.delete('1.0', tk.END)
    a = first_number.get()
    b = second_number.get()
    print(b)
    if a and b:
        if convertstr(b) == 0:
            result = "you can not divide by zero!!"
        else:
            result = convertstr(a)/convertstr(b)
    else:
        result = "insert both numbers"
    result_box.insert(tk.INSERT, result)
    first_number.set('')
    second_number.set('')


"""labels """

tk.Label(text='Insert first number').grid(row=0, column=0)
tk.Label(text='Insert second number').grid(row=1, column=0)

"""string variables"""

first_number = tk.StringVar()
second_number = tk.StringVar()


entry_first_number = tk.Entry(root, textvariable=first_number).grid(row=0, column = 1)
entry_second_number = tk.Entry(root, textvariable=second_number).grid(row=1, column=1)


"""buttons"""
child = tk.PanedWindow()
child.grid(row=2, column=0, sticky=tk.N)
tk.Button(child, text='+', command=add).grid(row=2, column=0)
tk.Button(child, text='-', command=substract).grid(row=2, column=1)
tk.Button(child, text='*', command=multiply ).grid(row=2, column=2)
tk.Button(child, text='/',command=divide).grid(row=2, column=3)
tk.Label(text='Result').grid(row=3, column=0)

"""result box"""
result_box = tk.Text(root)
result_box.grid(row=3, column=1)
result_box.config(width=10, height=5)

root.mainloop()

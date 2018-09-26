import tkinter as tk

root = tk.Tk()
colour = 'cyan'
root.configure(background=colour, width=50)
button_width = 7
button_height = 3
first_number = 0
#second_number = 0
operator = ""


"""insert box & result box"""
#pierwsza_liczba = tk.StringVar()
#druga_liczba = tk.StringVar()
result_box = tk.Text(root)
result_box.grid(row=0, column=0)
result_box.config(width=30, height=3)
insert_box = tk.Text(root)
insert_box.grid(row=1, column=0)
insert_box.config(width=30, height=3)


def convertstr(s):
    """Convert string to either int or float."""
    try:
        result = int(s)
    except ValueError:
        result = float(s)
    return result


def add():
    result_box.delete('1.0', tk.END)
    a = insert_box.get('1.0', tk.END)
    a = a[0:-1]
    globals()["first_number"] = a
    globals()["operator"] = "+"
    insert = a+"+"
    result_box.insert(tk.INSERT, insert)
    insert_box.delete('1.0', tk.END)


def substract():
    result_box.delete('1.0', tk.END)
    a = insert_box.get('1.0', tk.END)
    a = a[0:-1]
    globals()["first_number"] = a
    globals()["operator"] = "-"
    insert = a + "-"
    result_box.insert(tk.INSERT, insert)
    insert_box.delete('1.0', tk.END)


def multiply():
    result_box.delete('1.0', tk.END)
    a = insert_box.get('1.0', tk.END)
    a = a[0:-1]
    globals()["first_number"] = a
    globals()["operator"] = "*"
    insert = a + "*"
    result_box.insert(tk.INSERT, insert)
    insert_box.delete('1.0', tk.END)


def divide():
    result_box.delete('1.0', tk.END)
    a = insert_box.get('1.0', tk.END)
    a = a[0:-1]
    globals()["first_number"] = a
    globals()["operator"] = '/'
    insert = a + "/"
    result_box.insert(tk.INSERT, insert)
    insert_box.delete('1.0', tk.END)


def result_of_operation():
    second_number = insert_box.get('1.0', tk.END)
    second_number = second_number[0:-1]
    #print(str(second_number))
    #print(operator == '/')
    #print(str(second_number) == str(0))
    #print("type of second_number", type(second_number))
    #print(second_number)
    #print("type of opertor", type(operator))
    #print(operator)
    if operator == '+':
        result = convertstr(first_number)+convertstr(second_number)
    elif operator == '-':
        result = convertstr(first_number) - convertstr(second_number)
    elif operator == '*':
        result = convertstr(first_number) * convertstr(second_number)
    elif operator == '/' and second_number == "0":
        result = "you can not divide by zero"
    else:
        print('tutaj')
        result = convertstr(first_number)/convertstr(second_number)
    result = first_number+operator+second_number+'='+str(result)
    result_box.delete('1.0', tk.END)
    insert_box.delete('1.0', tk.END)
    result_box.insert(tk.INSERT, result)


def clear():
    insert_box.delete('1.0', tk.END)
    result_box.delete('1.0', tk.END)


def back():
    insert_box.delete('end - 2 chars')
    result_box.delete('end - 2 chars')


def insert_zero():
    insert_box.insert(tk.INSERT, 0)


def insert_one():
    insert_box.insert(tk.INSERT, 1)


def insert_two():
    insert_box.insert(tk.INSERT, 2)


def insert_three():
    insert_box.insert(tk.INSERT, 3)


def insert_four():
    insert_box.insert(tk.INSERT, 4)


def insert_five():
    insert_box.insert(tk.INSERT, 5)


def insert_six():
    insert_box.insert(tk.INSERT, 6)


def insert_seven():
    insert_box.insert(tk.INSERT, 7)


def insert_eight():
    insert_box.insert(tk.INSERT, 8)


def insert_nine():
    insert_box.insert(tk.INSERT, 9)


def back():
    result_box.delete('end - 2 chars')
    insert_box.delete('end - 2 chars')


def coma():
    if '.' not in insert_box.get('1.0', tk.END):
        insert_box.insert(tk.INSERT, '.')


"""buttons"""
child = tk.PanedWindow()
child.grid(row=2, column=0, sticky=tk.N)

# first row of buttons
tk.Button(child, text='CE', width=button_width, height=button_height).grid(row=2, column=0)
tk.Button(child, text='C', command=clear, width=button_width, height=button_height).grid(row=2, column=1)
tk.Button(child, text='Back', command=back, width=button_width, height=button_height).grid(row=2, column=2)
tk.Button(child, text='/', width=button_width, height=button_height, command=divide).grid(row=2, column=3)

# second row of buttons
tk.Button(child, text='7', command=insert_seven, width=button_width, height=button_height).grid(row=3, column=0)
tk.Button(child, text='8', command=insert_eight, width=button_width, height=button_height).grid(row=3, column=1)
tk.Button(child, text='9', command=insert_nine, width=button_width, height=button_height).grid(row=3, column=2)
tk.Button(child, text='*', width=button_width, height=button_height, command=multiply).grid(row=3, column=3)

# third row of buttons
tk.Button(child, text='4', command=insert_four, width=button_width, height=button_height).grid(row=4, column=0)
tk.Button(child, text='5', command=insert_five, width=button_width, height=button_height).grid(row=4, column=1)
tk.Button(child, text='6', command=insert_six, width=button_width, height=button_height).grid(row=4, column=2)
tk.Button(child, text='-', width=button_width, height=button_height, command=substract).grid(row=4, column=3)

# fourth row of buttons
tk.Button(child, text='1', command=insert_one, width=button_width, height=button_height).grid(row=5, column=0)
tk.Button(child, text='2', command=insert_two, width=button_width, height=button_height).grid(row=5, column=1)
tk.Button(child, text='3', command=insert_three, width=button_width, height=button_height).grid(row=5, column=2)
tk.Button(child, text='+', width=button_width, height=button_height, command=add).grid(row=5, column=3)

# fifth row of buttons
tk.Button(child, text='+-', width=button_width, height=button_height).grid(row=6, column=0)
tk.Button(child, text='0', command=insert_zero, width=button_width, height=button_height).grid(row=6, column=1)
tk.Button(child, text='.', width=button_width, height=button_height, command=coma).grid(row=6, column=2)
tk.Button(child, text='=', width=button_width, height=button_height, command=result_of_operation).grid(row=6, column=3)

# tk.Label(text='Result').grid(row=3, column=0)

"""result box"""
# result_box = tk.Text(root)
# result_box.grid(row=3, column=1)
# result_box.config(width=10, height=5)

root.mainloop()

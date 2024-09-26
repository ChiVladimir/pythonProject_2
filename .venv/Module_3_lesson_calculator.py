# Функции в Phyhon. Практика - Калькулятор
import tkinter as tk

def get_values():
    num1 = float(number1_entry.get())
    num2 = float(number2_entry.get())
    return num1, num2

def insert_values(result):
    answr_output.delete(0, 'end')
    answr_output.insert(0, result)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


window = tk.Tk()
window.title('My Calculator')
window.geometry("350x350")
window.resizable(False, False)

button_add = tk.Button(window, text="+", width = 3, height = 3, command=add)
button_add.place(x=280, y=100)
button_sub = tk.Button(window, text="-", width = 3, height = 3, command=sub)
button_sub.place(x=280, y=160)
button_mul = tk.Button(window, text="x", width = 3, height = 3, command=mul)
button_mul.place(x=280, y=220)
button_div = tk.Button(window, text="/", width = 3, height = 3, command=div)
button_div.place(x=280, y=280)


number1_entry = tk.Entry(window, width = 28)
number1_entry.place(x=10, y=100)
number1_txt = tk.Label(window, text = 'Enter the first number:')
number1_txt.place(x=10, y=80)

number2_entry = tk.Entry(window, width = 28)
number2_entry.place(x=10, y=150)
number2_txt = tk.Label(window, text = 'Enter the second number:')
number2_txt.place(x=10, y=130)

answr_output = tk.Entry(window, width = 28)
answr_output.place(x=10, y=250)
answr_txt = tk.Label(window, text = 'Press button [+], [-], [x] or [/] for result:')
answr_txt.place(x=10, y=230)


window.mainloop()
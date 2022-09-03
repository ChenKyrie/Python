# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.font as tkFont

def cal_bmi():
    height = float(height_input.get())/100
    weight = float(weight_input.get())
    bmi = weight / height**2
    bmi = round(bmi, 1)
    bmi_label["text"] = f'您的bmi:{bmi}'

window = Tk()
window.title('BMI計算機')
window.geometry('230x300')
window.config(padx=50, pady=50)

height_label = Label(text='身高')
height_label.grid(row=0, column=0)

height_input = Entry(width=10)
height_input.grid(row=0, column=1)

cm_label = Label(text='公分')
cm_label.grid(row=0, column=2)

weight_label = Label(text='體重')
weight_label.grid(row=1, column=0)

weight_input = Entry(width=10)
weight_input.grid(row=1, column=1)

kg_label = Label(text='公斤')
kg_label.grid(row=1, column=2)

bmi_label = Label(text='您的BMI:0')
bmi_label.grid(row=2, column=1)

button = Button(text='計算', command=cal_bmi)
button.grid(row=3, column=1)


window.mainloop()

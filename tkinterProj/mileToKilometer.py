from tkinter import *


def calculate():
    value = float(input.get())
    one_mile_in_km = 1.609344
    result = one_mile_in_km * value
    display.config(text=str(result)+" KM")


window = Tk()
window.title("mile to KM")
window.minsize(300, 150)
window.config(padx=50, pady=50)

head_label = Label(text="convert miles to KM")
head_label.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=0, row=1)

input = Entry()
input.grid(column=1, row=1)

button = Button(text="convert", command=calculate)
button.grid(column=1,row=2)

km_label = Label(text="Is Equal to ")
km_label.grid(column=0, row=3)

display = Label()
display.grid(column=1,row=3)

window.mainloop()

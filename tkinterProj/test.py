from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)



window = Tk()
window.title("my window")
window.minsize(500,300)
window.config(padx=50,pady=50)

my_label = Label(text = "This is my label",font=('Arial',10,'bold'))
my_label.grid(column=0,row=0)

button = Button(text="click me",command=button_clicked)
button.grid(column=1,row=0)


input =Entry(width=20)
print(input.get())
input.grid(column=2,row=0)
window.mainloop()
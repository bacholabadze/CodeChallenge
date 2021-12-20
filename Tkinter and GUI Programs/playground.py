from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=600, height=600)
window.config(padx=10, pady=10)

# Label
my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))

my_label['text'] = 'new text'
my_label.config(text='newest text')
# my_label.pack()
my_label.grid(column=0, row=0)
# Button


def button_clicked():
    my_label.config(text=input_field.get())


button = Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text='Click Me too')
new_button.grid(column=2, row=0)

# Entry
input_field = Entry(width=10)
input_field.grid(column=3, row=2)

window.mainloop()

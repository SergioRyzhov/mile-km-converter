from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

# label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)
my_label["text"] = "New Text"
my_label.config(text="New Text")

# button


def button_clicked():
    label_text = input.get()
    my_label.config(text=label_text)


my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(row=1, column=1)

# entry

input = Entry(width=10)
input.grid(row=2, column=3)


new_button = Button(text="New Button")
new_button.grid(row=0, column=2)


window.mainloop()

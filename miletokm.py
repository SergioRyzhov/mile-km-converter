from tkinter import *


def button_clicked():
    result = round(float(input.get()) * 1.609, 1)
    output_label.config(text=result)


window = Tk()
window.title("Converter Miles to Km")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(row=0, column=3)

km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(row=1, column=3)

equals_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equals_label.grid(row=1, column=0)

input = Entry(width=10)
input.grid(row=0, column=1)

output_label = Label(text="", font=("Arial", 14))
output_label.grid(row=1, column=1)

button = Button(text="Calculate", font=("Arial", 12, "bold"), command=button_clicked)
button.grid(row=2, column=1)

window.mainloop()

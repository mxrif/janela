from tkinter import Tk, Button, Label, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime

def clicked():
    global entry
    date = entry.get()
    # data precisa estar no formato específico '___(mês c/ 3 letras) __(dia),(espaço) ____(ano) para funcionar.
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    showinfo(message='{} was a {}'.format(date, weekday))

root = Tk()
label = Label(root, text='Geben Sie ein Datum ein:')
label.grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)
button = Button(root, text='Klicken', command=clicked)
button.grid(row=1, column=0, columnspan=2)
root.mainloop()


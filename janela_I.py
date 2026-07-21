from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage(file='photo.gif').subsample(1)
image = Label(master=root, image=photo)
image.pack(side=TOP)
text = Label(master=root, font=("Courier", 18), text='Folipurba ist richtig cool')
text.pack(side=BOTTOM)
# roda a janela
root.mainloop()


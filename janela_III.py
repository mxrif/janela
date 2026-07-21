from tkinter import Tk, Button, Label
from tkinter.messagebox import showinfo
from time import strftime, localtime

# tamanho da tela
largura_tela = 1280
altura_tela = 800

# posição da janela na tela
x = (largura_tela - 100) // 2
y = (altura_tela - 80) // 2

def clicked():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
    showinfo(message=time)

root = Tk()

# tamanho da janela e posição na tela
root.geometry(f"100x80+{x}+{y}")

# abre a janela na frente e foca
root.lift()
root.focus_force()

button = Button(root, text="Klicken", command=clicked)
button.pack()
root.mainloop()
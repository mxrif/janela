from tkinter import Tk, Label, RAISED
root = Tk()

# tamanho da tela
largura_tela = 1280
altura_tela = 800

# posição da janela na tela
x = (largura_tela - 100) // 2
y = (altura_tela - 80) // 2

# tamanho da janela e posição na tela
root.geometry(f"100x80+{x}+{y}")

#listas/botões
labels = [['1','2','3'], ['4','5','6'], ['7','8','9'], ['*','0','#']]
for r in range(4):
    for c in range(3):
        label = Label(root, relief=RAISED, padx=10, pady=0, text=labels[r][c])
        label.grid(row=r, column=c)
# abre a janela na frente e foca
root.lift()
root.focus_force()
# laço principal
root.mainloop()
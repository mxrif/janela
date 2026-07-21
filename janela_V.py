from tkinter import Tk, Text, BOTH

def key_pressed(event):
    print('char: {}'.format(event.keysym))

def mouse_clicked_left(event):
    print('linke Maustaste angeklickt')

def mouse_clicked_right(event):
    print('rechte Maustaste geklickt')

root = Tk()
text = Text(root, width=20, height=5)
text.bind('<KeyPress>', key_pressed)
text.bind('<Button-1>', mouse_clicked_left)
text.bind('<Button-2>', mouse_clicked_right)
# mesmo com expand=False ainda expande na vertical por causa do .pack, fill=both preenche o espaço
text.pack(expand=True, fill=BOTH)
root.mainloop()
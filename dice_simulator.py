from tkinter import Tk, Label, Button
from random import randint, choice
from PIL import Image, ImageTk
from time import sleep

def get_number():
    image1 = Image.open(f'{randint(1,6)}.png')
    photo1 = ImageTk.PhotoImage(image1)
    pic1.configure(image=photo1)
    pic1.image = photo1
    button1.configure(activebackground=choice(colorlis))

if __name__ == '__main__':
    root = Tk()
    root.title('Dice Simulator')
    root.geometry('400x400')
    root.configure(background='orange')
    icon = ImageTk.PhotoImage(file='icon.png')
    root.iconphoto(False, icon)

    Label(root,text='Dice Simulator',bg='orange', font='arial 20 bold', padx='5', pady='5').pack(padx='10', pady='10')
    image1 = Image.open('lets play.png')
    photo1 = ImageTk.PhotoImage(image1)
    pic1 = Label(image=photo1, bg='red')
    pic1.image = photo1
    pic1.pack(pady=10,padx=5, expand=True)

    colorlis = ['red','green','yellow','blue']
    button1 = Button(root, text='Roll the dice', font='arial 15',activebackground = choice(colorlis), command=get_number)
    button1.pack(expand = True)

    root.mainloop()
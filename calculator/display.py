import tkinter as tk
from PIL import Image, ImageTk
from tkinter.font import Font
from calculator.pressed import *
import calculator.calcul as calcul
from calculator import root

def display():
    canva = tk.Canvas(root, width = 523, height = 688)
    canva.grid(column=1, rowspan=1)

    root.title("My calculator")
    root.minsize(523, 688)
    # background 
    background = tk.PhotoImage(file = "/home/jk1234/Documents/YNOV/calculator/calculator/static/img/background.png")
    background_label = tk.Label(image = background)

    # logo 
    root.iconphoto(False, tk.PhotoImage(file='/home/jk1234/Documents/YNOV/calculator/calculator/static/img/xingxinlogo.PNG'))
    logo = Image.open("/home/jk1234/Documents/YNOV/calculator/calculator/static/img/xingxinlogo2.PNG")
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo 

    cop = "#59606A"
    cnumb = "#E0E0E0"
    gFont = ("Arial", 12)
    DisplayFont = Font(
        family = "Modern LCD-7",
        size = 15
        ),
    #création des boutons
    button_C = tk.Button(root, text = "C", width = 11, height = 2, font =gFont, bg = cop, command = pressedC)
    button_undo = tk.Button(root, text = "retour", width = 11, height = 2, font =gFont, bg = cop, command = pressedBack)
    button_div = tk.Button(root, text = "/", width = 11, height = 2, font =gFont, bg = cop, command = pressedDiv)
    button_7 = tk.Button(root, text = "7", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedSeven)
    button_8 = tk.Button(root, text = "8", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedEight)
    button_9 = tk.Button(root, text = "9", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedNine)
    button_multi = tk.Button(root, text = "x", width = 11, height = 2, font =gFont, bg = cop, command = pressedMulti)
    button_4 = tk.Button(root, text = "4", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedFour)
    button_5 = tk.Button(root, text = "5", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedFive)
    button_6 = tk.Button(root, text = "6", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedSix)
    button_minus = tk.Button(root, text = "-", width =  11, height = 2, font =gFont, bg = cop, command = pressedMinus)
    button_1 = tk.Button(root, text = "1", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedOne)
    button_2 = tk.Button(root, text = "2", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedTwo)
    button_3 = tk.Button(root, text = "3", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedThree)
    button_plus = tk.Button(root, text = "+", width = 11, height = 2, font =gFont, bg = cop, command = pressedPlus)
    button_0 = tk.Button(root, text = "0", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedZero)
    button_comma = tk.Button(root, text = ",", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedComma)
    button_modulo = tk.Button(root, text = "%", width = 11, height = 2, font =gFont, bg = cop, command = pressedModulo)
    button_equal = tk.Button(root, text = "=", width = 11, height = 2, font =gFont, bg = cop, command = calcul.result)
    # 
    resultlabel = tk.Label(root, textvariable = resulttext, font =DisplayFont, fg= "#000000", bg = "#C0C0C0")
    operationlabel = tk.Label(root, textvariable = operationtext, font =DisplayFont, fg = "#000000", bg = "#C0C0C0")
    # 
    #placement décor
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    logo_label.place(x=60, y=200, relwidth=0.17, relheight=0.11)

    #écran
    # 
    operationlabel.place(x=60, y=90, relwidth=0.774, relheight=0.07)
    resultlabel.place(x=60, y=140, relwidth=0.774, relheight=0.07)
    # 

    button_undo.place(x=414, y=365, relwidth=0.13, relheight=0.078)
    button_C.place(x=325, y=365, relwidth=0.13, relheight=0.078)

    #numbers
    button_0.place(x=45, y=581, relwidth=0.13, relheight=0.078)
    button_1.place(x=45, y=510, relwidth=0.13, relheight=0.078)
    button_2.place(x=135, y=510, relwidth=0.13, relheight=0.078)
    button_3.place(x=225, y=510, relwidth=0.13, relheight=0.078)
    button_4.place(x=45, y=437, relwidth=0.13, relheight=0.078)
    button_5.place(x=135, y=437, relwidth=0.13, relheight=0.078)
    button_6.place(x=225, y=437, relwidth=0.13, relheight=0.078)
    button_7.place(x=45, y=365, relwidth=0.13, relheight=0.078)
    button_8.place(x=135, y=365, relwidth=0.13, relheight=0.078)
    button_9.place(x=225, y=365, relwidth=0.13, relheight=0.078)
    button_comma.place(x=225, y=581, relwidth=0.13, relheight=0.078)

    #operators
    button_multi.place(x=325, y=437, relwidth=0.13, relheight=0.078)
    button_div.place(x=414, y=437, relwidth=0.13, relheight=0.078)
    button_minus.place(x=414, y=510, relwidth=0.13, relheight=0.078)
    button_plus.place(x=325, y=510, relwidth=0.13, relheight=0.078)
    button_equal.place(x=414, y=581, relwidth=0.13, relheight=0.078)
    button_modulo.place(x=325, y=581, relwidth=0.13, relheight=0.078)
    root.mainloop()

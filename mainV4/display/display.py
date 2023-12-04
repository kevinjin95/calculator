import tkinter as tk
from PIL import Image, ImageTk
from tkinter.font import Font
import pressed.pressed as pressed
import calcul.calcul as calcul
import mainV4 as main

def display(root):
    canva = tk.Canvas(root, width = 523, height = 688)
    canva.grid(column=1, rowspan=1)

    root.title("My calculator")
    root.minsize(523, 688)
    # background 
    background = tk.PhotoImage(file = "assets/img/background.png")
    background_label = tk.Label(image = background)

    # logo 
    root.iconbitmap("assets/img/xingxinlogo.ico")
    logo = Image.open("assets/img/xingxinlogo2.png")
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
    button_C = tk.Button(root, text = "C", width = 11, height = 2, font =gFont, bg = cop, command=pressed.pressedC)
    button_undo = tk.Button(root, text = "retour", width = 11, height = 2, font =gFont, bg = cop, command = pressed.pressedback)
    button_div = tk.Button(root, text = "/", width = 11, height = 2, font =gFont, bg = cop, command = pressed.pressedDiv)
    button_7 = tk.Button(root, text = "7", width = 11, height = 2, font =gFont, bg = cnumb, command = pressed.pressedSeven)
    button_8 = tk.Button(root, text = "8", width = 11, height = 2, font =gFont, bg = cnumb, command = pressed.pressedEight)
    button_9 = tk.Button(root, text = "9", width = 11, height = 2, font =gFont, bg = cnumb, command = pressed.pressedNine)
    button_multi = tk.Button(root, text = "x", width = 11, height = 2, font =gFont, bg = cop, command = pressed.pressedMulti)
    button_4 = tk.Button(root, text = "4", width = 11, height = 2, font =gFont, bg = cnumb, command = pressed.pressedFour)
    button_5 = tk.Button(root, text = "5", width = 11, height = 2, font =gFont, bg = cnumb, command = pressed.pressedFive)
    button_6 = tk.Button(root, text = "6", width = 11, height = 2, font =gFont, bg = cnumb, command = pressed.pressedSix)
    button_minus = tk.Button(root, text = "-", width =  11, height = 2, font =gFont, bg = cop, command = pressed.pressedMinus)
    button_1 = tk.Button(root, text = "1", width = 11, height = 2, font =gFont, bg = cnumb, command = pressed.pressedOne)
    button_2 = tk.Button(root, text = "2", width = 11, height = 2, font =gFont, bg = cnumb, command = pressed.pressedTwo)
    button_3 = tk.Button(root, text = "3", width = 11, height = 2, font =gFont, bg = cnumb, command = pressed.pressedThree)
    button_plus = tk.Button(root, text = "+", width = 11, height = 2, font =gFont, bg = cop, command = pressed.pressedPlus)
    button_0 = tk.Button(root, text = "0", width = 11, height = 2, font =gFont, bg = cnumb, command = pressed.pressedZero)
    button_comma = tk.Button(root, text = ",", width = 11, height = 2, font =gFont, bg = cnumb, command = pressed.pressedComma)
    button_modulo = tk.Button(root, text = "%", width = 11, height = 2, font =gFont, bg = cop, command = pressed.pressedModulo)
    button_equal = tk.Button(root, text = "=", width = 11, height = 2, font =gFont, bg = cop, command = calcul.result)
    # 
    resultlabel = tk.Label(root, textvariable = main.resulttext, font =DisplayFont, fg= "#000000", bg = "#C0C0C0")
    operationlabel = tk.Label(root, textvariable = main.operationtext, font =DisplayFont, fg = "#000000", bg = "#C0C0C0")
    # 
    #placement décor
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    logo_label.place(x=80, y=220, relwidth=0.15, relheight=0.09)

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

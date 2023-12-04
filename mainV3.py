import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from colorama import Fore, init
from tkinter.font import Font

root = tk.Tk()
numbers = []
deconcat_number = []
entered_operators = []
operationlist = []
last_Pressed = []
resulttext = tk.StringVar()
operationtext = tk.StringVar()

def pressedComma() :
    deconcat_number.append(".")
    operationlist.append(".")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("number")

def pressedZero() :
    deconcat_number.append("0")
    operationlist.append("0")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("number")

def pressedOne() :
    deconcat_number.append("1")
    operationlist.append("1")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("number")

def pressedTwo() :
    deconcat_number.append("2")
    operationlist.append("2")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("number")

def pressedThree() :
    deconcat_number.append("3")
    operationlist.append("3")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("number")

def pressedFour() :
    deconcat_number.append("4")
    operationlist.append("4")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("number")

def pressedFive() :
    deconcat_number.append("5")
    operationlist.append("5")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("number")

def pressedSix() :
    deconcat_number.append("6")
    operationlist.append("6")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("number")

def pressedSeven() :
    deconcat_number.append("7")
    operationlist.append("7")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("number")

def pressedEight() :
    deconcat_number.append("8")
    operationlist.append("8")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("number")

def pressedNine() :
    deconcat_number.append("9")
    operationlist.append("9")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("number")

def pressedPlus() :
    concat_number = "".join (deconcat_number)
    if len(concat_number) >= 0:
        numbers.append(concat_number)
    deconcat_number.clear()
    concat_number = None
    entered_operators.append("+")
    operationlist.append("+")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("operator")

def pressedMinus() :
    concat_number = "".join (deconcat_number)
    if len(concat_number) >= 0:
        numbers.append(concat_number)
    deconcat_number.clear()
    concat_number = None
    entered_operators.append("-")
    operationlist.append("-")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("operator")

def pressedMulti() :
    concat_number = "".join (deconcat_number)
    if len(concat_number) >= 0:
        numbers.append(concat_number)
    deconcat_number.clear()
    concat_number = None
    entered_operators.append("x")
    operationlist.append("x")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("operator")

def pressedDiv() :
    concat_number = "".join (deconcat_number)
    if len(concat_number) >= 0:
        numbers.append(concat_number)
    deconcat_number.clear()
    concat_number = None
    entered_operators.append("/")
    operationlist.append("/")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("operator")

def pressedModulo() :
    concat_number = "".join (deconcat_number)
    if len(concat_number) >= 0:
        numbers.append(concat_number)
    deconcat_number.clear()
    concat_number = None
    entered_operators.append("%")
    operationlist.append("%")
    str2tkstr()
    last_Pressed.clear()
    last_Pressed.append("operator")

def str2tkstr():
    operationstr = "".join (operationlist)
    operationtext.set(operationstr)
    print(operationstr)

def pressedC():
    operationtext.set("")
    resulttext.set("")
    entered_operators.clear()
    operationlist.clear()
    deconcat_number.clear()
    numbers.clear()
    deconcat_number.clear()

def pressedback() :
    print("last pressed : ", last_Pressed)
    operationlist.pop(len(operationlist)-1)
    operationstr = operationlist
    operationtext.set(operationstr)
    if last_Pressed[0] == "number":
        deconcat_number.pop(len(deconcat_number)-1)
        print(deconcat_number)
    elif last_Pressed[0] == "operator":
        print(entered_operators)
        entered_operators.pop(len(entered_operators)-1)
        deconcat_number.append(numbers[len(numbers)-1])
        numbers.pop(len(numbers)-1)
        print(entered_operators)

def multiOrDiv():
    i = 0
    concat_number = "".join (deconcat_number)
    numbers.append(concat_number)
    last_Pressed.clear()
    last_Pressed.append("operator")
    while True:
        print("")
        print("numbers :", numbers)
        print("operators : ", entered_operators, ", index: ", i)
        if isinstance(numbers[i], int) == True :
            number1 = int(numbers[i])
        else:
            number1 = float(numbers[i])

        if isinstance(numbers[i+1], int) == True :
            number2 = int(numbers[i+1])
        else:
            number2 = float(numbers[i+1])
        print("number1: ", number1, ", number2: ", number2)
        if entered_operators[i] == "x" :
            numbers[i] = number1 * number2
            numbers.remove(numbers[i+1])
            entered_operators.remove(entered_operators[i])

        elif entered_operators[i] == "/":
            numbers[i] = number1 / number2
            numbers.remove(numbers[i+1])
            entered_operators.remove(entered_operators[i])
           
        else:
            print("jump")
            i += 1

        if i > len(entered_operators)-1:
            print("multidiv out")
            break
       
def result():
    print("result")
    multiOrDiv()
    print("sorti!!")
    print("no more !")
    while True:                           
        if len(entered_operators) != 0:
            if entered_operators[0] == "+":
                if isinstance(numbers[0], int) == True :
                    number1 = int(numbers[0])
                else:
                    number1 = float(numbers[0])

                if isinstance(numbers[1], int) == True :
                    number2 = int(numbers[1])
                else:
                    number2 = float(numbers[1])

                numbers[0] = sum([number1, number2])
                numbers.remove(numbers[1])
                entered_operators.remove(entered_operators[0])
            elif entered_operators[0] == "-":
                if isinstance(numbers[0], int) == True :
                    number1 = int(numbers[0])
                else:
                    number1 = float(numbers[0])
                    
                if isinstance(numbers[1], int) == True :
                    number2 = int(numbers[1])
                else:
                    number2 = float(numbers[1])
                numbers[0] = number1 - number2
                numbers.remove(numbers[1])
                entered_operators.remove(entered_operators[0])
            elif entered_operators[0] == "%":
                if isinstance(numbers[0], int) == True :
                    number1 = int(numbers[0])
                else:
                    number1 = float(numbers[0])

                if isinstance(numbers[1], int) == True :
                    number2 = int(numbers[1])
                else:
                    number2 = float(numbers[1])

                numbers[0] =  number1 % number2
                numbers.remove(numbers[1])
                entered_operators.remove(entered_operators[0])
        if len(entered_operators) == 0:
            resultValue = numbers[0]
            entered_operators.clear()
            break
    print("result: ")
    print(numbers[0])
    resulttext.set(resultValue)

def main():
    main = tk.Canvas(root, width = 523, height = 688)
    main.grid(column=1, rowspan=1)

    root.title("My calculator")
    root.minsize(523, 688)
    # background 
    background = tk.PhotoImage(file = "C://Users//Kevin//Documents//cours_ynov//ydays_prog_ludique//calculatrice//background.png")
    background_label = tk.Label(image = background)

    # logo 
    root.iconbitmap("xingxinlogo.ico")
    logo = Image.open("C://Users//Kevin//Documents//cours_ynov//ydays_prog_ludique//calculatrice//xingxinlogo2.png")
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
    button_C = tk.Button(root, text = "C", width = 11, height = 2, font =gFont, bg = cop, command=pressedC)
    button_undo = tk.Button(root, text = "retour", width = 11, height = 2, font =gFont, bg = cop, command = pressedback)
    button_div = tk.Button(root, text = "/", width = 11, height = 2, font =gFont, bg = cop, command = pressedDiv)
    button_7 = tk.Button(root, text = "7", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedSeven)
    button_8 = tk.Button(root, text = "8", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedEight)
    button_9 = tk.Button(root, text = "9", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedNine)
    button_multi = tk.Button(root, text = "x", width = 11, height = 2, font =gFont, bg = cop, command = pressedMulti)
    button_4 = tk.Button(root, text = "4", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedFour)
    button_5 = tk.Button(root, text = "5", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedFive)
    button_6 = tk.Button(root, text = "6", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedSix)
    button_minus = tk.Button(root, text = "-", width = 11, height = 2, font =gFont, bg = cop, command = pressedMinus)
    button_1 = tk.Button(root, text = "1", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedOne)
    button_2 = tk.Button(root, text = "2", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedTwo)
    button_3 = tk.Button(root, text = "3", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedThree)
    button_plus = tk.Button(root, text = "+", width = 11, height = 2, font =gFont, bg = cop, command = pressedPlus)
    button_0 = tk.Button(root, text = "0", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedZero)
    button_comma = tk.Button(root, text = ",", width = 11, height = 2, font =gFont, bg = cnumb, command = pressedComma)
    button_modulo = tk.Button(root, text = "%", width = 11, height = 2, font =gFont, bg = cop, command = pressedModulo)
    button_equal = tk.Button(root, text = "=", width = 11, height = 2, font =gFont, bg = cop, command = result)
    resultlabel = tk.Label(root, textvariable = resulttext, font =DisplayFont, fg= "#000000", bg = "#C0C0C0")
    operationlabel = tk.Label(root, textvariable = operationtext, font =DisplayFont, fg = "#000000", bg = "#C0C0C0")

    #placement décor
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    logo_label.place(x=80, y=220, relwidth=0.15, relheight=0.09)

    #écran
    operationlabel.place(x=60, y=90, relwidth=0.774, relheight=0.07)
    resultlabel.place(x=60, y=140, relwidth=0.774, relheight=0.07)

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

if __name__=="__main__": 
    main()

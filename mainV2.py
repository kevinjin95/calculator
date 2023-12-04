# version compacté qui ne marche pas !!!
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from colorama import Fore, init
from tkinter.font import Font

root = tk.Tk()
operation = ""
numbers = []
deconcat_number = []
concat_number = []
entered_operators = []
operationlist = []
number1 = int
number2 = int
last_Pressed = []
resulttext = tk.StringVar()
operationtext = tk.StringVar()

def pressedNum(number) :
    deconcat_number.append(number)
    operationlist.append(number)
    # str2tkstr()
    print(deconcat_number)
    last_Pressed.clear()
    last_Pressed.append("number")

def pressedOperator(operator) :
    concat_number = "".join (deconcat_number)
    if len(concat_number) >= 0:
        numbers.append(concat_number)
    deconcat_number.clear()
    concat_number = None
    entered_operators.append(operator)
    operationlist.append(operator)
    # str2tkstr()
    print(entered_operators)
    print(numbers)
    last_Pressed.clear()
    last_Pressed.append("operator")

def str2tkstr():
    operationstr = "".join (operationlist)
    operationtext.set(operationstr)
    
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

def multidiv():
    concat_number = "".join (deconcat_number)
    numbers.append(concat_number)
    last_Pressed.clear()
    last_Pressed.append("operator")
    while True:
        if len(entered_operators) != 0:
            for i in range (len(entered_operators)):
                print("numbers :", numbers)
                print("operator : ",entered_operators)
                print("index : ", i)
                if entered_operators[int(i)] == "x" :
                    if isinstance(numbers[i], int) == True :
                        number1 = int(numbers[i])
                    else:
                        number1 = float(numbers[i])

                    if isinstance(numbers[i+1], int) == True :
                        number2 = int(numbers[i+1])
                    else:
                        number2 = float(numbers[i+1])
                    numbers[i] = number1 * number2
                    numbers.remove(numbers[i+1])    
                    entered_operators.remove(entered_operators[int(i)])
            break

def result():
    multidiv()
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
            elif entered_operators[0] == "/":
                if isinstance(numbers[0], int) == True :
                    number1 = int(numbers[0])
                else:
                    number1 = float(numbers[0])
                    
                if isinstance(numbers[1], int) == True :
                    number2 = int(numbers[1])
                else:
                    number2 = float(numbers[1])
                numbers[0] = number1 / number2
                numbers.remove(numbers[1])
                entered_operators.remove(entered_operators[0])
        if len(entered_operators) == 0:
            result = numbers[0]
            entered_operators.clear()
            deconcat_number.clear()
            numbers.clear()
            break
    resulttext.set(result)
    clear()


   
def clear():
    deconcat_number.clear()
    concat_number = None
    numbers.clear()
    deconcat_number.clear()
    result = None

def main():
    main = tk.Canvas(root, width = 523, height = 688)

    # background 
    main.grid(column=1, rowspan=1)
    background = tk.PhotoImage(file = "C://Users//Kevin//Documents//cours_ynov//ydays_prog_ludique//calculatrice//147972.png")
    background_label = tk.Label(image = background)

    # logo 
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
        )
    #création des boutons
    button_undo = tk.Button(root, text = "retour", width = 11, height = 2, font =gFont, bg = cop, command=pressedback)
    button_div = tk.Button(root, text = "/", width = 11, height = 2, font =gFont, bg = cop, command=pressedOperator("/"))
    button_7 = tk.Button(root, text = "7", width = 11, height = 2, font =gFont, bg = cnumb, command=pressedNum("7"))
    button_8 = tk.Button(root, text = "8", width = 11, height = 2, font =gFont, bg = cnumb, command=pressedNum("8"))
    button_9 = tk.Button(root, text = "9", width = 11, height = 2, font =gFont, bg = cnumb, command=pressedNum("9"))
    button_multi = tk.Button(root, text = "x", width = 11, height = 2, font =gFont, bg = cop, command=pressedOperator("*"))
    button_4 = tk.Button(root, text = "4", width = 11, height = 2, font =gFont, bg = cnumb, command=pressedNum("4"))
    button_5 = tk.Button(root, text = "5", width = 11, height = 2, font =gFont, bg = cnumb, command=pressedNum("5"))
    button_6 = tk.Button(root, text = "6", width = 11, height = 2, font =gFont, bg = cnumb, command=pressedNum("6"))
    button_minus = tk.Button(root, text = "-", width = 11, height = 2, font =gFont, bg = cop, command=pressedOperator("-"))
    button_1 = tk.Button(root, text = "1", width = 11, height = 2, font =gFont, bg = cnumb, command=pressedNum("1"))
    button_2 = tk.Button(root, text = "2", width = 11, height = 2, font =gFont, bg = cnumb, command=pressedNum("2"))
    button_3 = tk.Button(root, text = "3", width = 11, height = 2, font =gFont, bg = cnumb, command=pressedNum("3"))
    button_plus = tk.Button(root, text = "+", width = 11, height = 2, font =gFont, bg = cop, command=pressedOperator("+"))
    button_0 = tk.Button(root, text = "0", width = 11, height = 2, font =gFont, bg = cnumb, command=pressedNum("0"))
    button_comma = tk.Button(root, text = ",", width = 11, height = 2, font =gFont, bg = cnumb, command=pressedNum("."))
    button_equal = tk.Button(root, text = "=", width = 11, height = 2, font =gFont, bg = cop, command=result)
    resultlabel = tk.Label(root, textvariable = resulttext, font =DisplayFont, fg= "#000000", bg = "#C0C0C0")
    operationlabel = tk.Label(root, textvariable = operationtext, font =DisplayFont, fg = "#000000", bg = "#C0C0C0")

        #placement
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    logo_label.place(x=80, y=220, relwidth=0.15, relheight=0.09)

    #écran
    operationlabel.place(x=60, y=90, relwidth=0.774, relheight=0.07)
    resultlabel.place(x=60, y=140, relwidth=0.774, relheight=0.07)
    button_undo.place(x=414, y=365, relwidth=0.13, relheight=0.078)

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
    button_plus.place(x=325, y=510, relwidth=0.13, relheight=0.182)
    button_equal.place(x=414, y=581, relwidth=0.13, relheight=0.078)
    
    root.mainloop()

if __name__=="__main__": 
    main()

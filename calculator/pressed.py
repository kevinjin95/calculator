from calculator.value import *

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
    last_Pressed.append("number")

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
    last_Pressed.append("number")

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
    last_Pressed.append("number")

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
    last_Pressed.append("number")

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
    last_Pressed.append("number")

#permet à ce qui est tapé d'être affiché à l'écran
def str2tkstr(): 
    operationstr = "".join (operationlist)
    # 
    operationtext.set(operationstr)
    # 
    print(operationstr)

def pressedC():
    operationtext.set("")
    resulttext.set("")
    entered_operators.clear()
    operationlist.clear()
    deconcat_number.clear()
    numbers.clear()
    deconcat_number.clear()

def pressedBack() :
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

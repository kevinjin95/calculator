import value.value as value
import mainV4 as main

def pressedComma() :
    main.deconcat_number.append(".")
    main.operationlist.append(".")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

def pressedZero() :
    main.deconcat_number.append("0")
    main.operationlist.append("0")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

def pressedOne() :
    main.deconcat_number.append("1")
    main.operationlist.append("1")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

def pressedTwo() :
    main.deconcat_number.append("2")
    main.operationlist.append("2")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

def pressedThree() :
    main.deconcat_number.append("3")
    main.operationlist.append("3")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

def pressedFour() :
    main.deconcat_number.append("4")
    main.operationlist.append("4")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

def pressedFive() :
    main.deconcat_number.append("5")
    main.operationlist.append("5")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

def pressedSix() :
    main.deconcat_number.append("6")
    main.operationlist.append("6")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

def pressedSeven() :
    main.deconcat_number.append("7")
    main.operationlist.append("7")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

def pressedEight() :
    main.deconcat_number.append("8")
    main.operationlist.append("8")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

def pressedNine() :
    main.deconcat_number.append("9")
    main.operationlist.append("9")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

def pressedPlus() :
    concat_number = "".join (main.deconcat_number)
    if len(concat_number) >= 0:
        main.numbers.append(concat_number)
    main.deconcat_number.clear()
    concat_number = None
    main.entered_operators.append("+")
    main.operationlist.append("+")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

def pressedMinus() :
    concat_number = "".join (main.deconcat_number)
    if len(concat_number) >= 0:
        main.numbers.append(concat_number)
    main.deconcat_number.clear()
    concat_number = None
    main.entered_operators.append("-")
    main.operationlist.append("-")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

def pressedMulti() :
    concat_number = "".join (main.deconcat_number)
    if len(concat_number) >= 0:
        main.numbers.append(concat_number)
    main.deconcat_number.clear()
    concat_number = None
    main.entered_operators.append("x")
    main.operationlist.append("x")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

def pressedDiv() :
    concat_number = "".join (main.deconcat_number)
    if len(concat_number) >= 0:
        main.numbers.append(concat_number)
    main.deconcat_number.clear()
    concat_number = None
    main.entered_operators.append("/")
    main.operationlist.append("/")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

def pressedModulo() :
    concat_number = "".join (main.deconcat_number)
    if len(concat_number) >= 0:
        main.numbers.append(concat_number)
    main.deconcat_number.clear()
    concat_number = None
    main.entered_operators.append("%")
    main.operationlist.append("%")
    str2tkstr()
    main.last_Pressed.clear()
    main.last_Pressed.append("number")

#permet à ce qui est tapé d'être affiché à l'écran
def str2tkstr(): 
    operationstr = "".join (main.operationlist)
    # 
    main.operationtext.set(operationstr)
    # 
    print(operationstr)

def pressedC():
    main.operationtext.set("")
    main.resulttext.set("")
    main.entered_operators.clear()
    main.operationlist.clear()
    main.deconcat_number.clear()
    main.numbers.clear()
    main.deconcat_number.clear()

def pressedback() :
    print("last pressed : ", main.last_Pressed)
    main.operationlist.pop(len(main.operationlist)-1)
    operationstr = main.operationlist
    main.operationtext.set(operationstr)
    if main.last_Pressed[0] == "number":
        main.deconcat_number.pop(len(main.deconcat_number)-1)
        print(main.deconcat_number)
    elif main.last_Pressed[0] == "operator":
        print(main.entered_operators)
        main.entered_operators.pop(len(main.entered_operators)-1)
        main.deconcat_number.append(main.numbers[len(main.numbers)-1])
        main.numbers.pop(len(main.numbers)-1)
        print(main.entered_operators)

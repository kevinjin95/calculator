from calculator.value import *
from calculator import root

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
    # 
    resulttext.set(resultValue)
    # 
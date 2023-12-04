import value.value as value
import mainV4 as main

def multiOrDiv():
    i = 0
    concat_number = "".join (value.deconcat_number)
    value.numbers.append(concat_number)
    value.last_Pressed.clear()
    value.last_Pressed.append("operator")
    while True:
        print("")
        print("numbers :", value.numbers)
        print("operators : ", value.entered_operators, ", index: ", i)
        if isinstance(value.numbers[i], int) == True :
            number1 = int(value.numbers[i])
        else:
            number1 = float(value.numbers[i])

        if isinstance(value.numbers[i+1], int) == True :
            number2 = int(value.numbers[i+1])
        else:
            number2 = float(value.numbers[i+1])
        print("number1: ", number1, ", number2: ", number2)
        if value.entered_operators[i] == "x" :
            value.numbers[i] = number1 * number2
            value.numbers.remove(value.numbers[i+1])
            value.entered_operators.remove(value.entered_operators[i])

        elif value.entered_operators[i] == "/":
            value.numbers[i] = number1 / number2
            value.numbers.remove(value.numbers[i+1])
            value.entered_operators.remove(value.entered_operators[i])
           
        else:
            print("jump")
            i += 1

        if i > len(value.entered_operators)-1:
            print("multidiv out")
            break
       
def result():
    print("result")
    multiOrDiv()
    print("sorti!!")
    print("no more !")
    while True:                           
        if len(value.entered_operators) != 0:
            if value.entered_operators[0] == "+":
                if isinstance(value.numbers[0], int) == True :
                    number1 = int(value.numbers[0])
                else:
                    number1 = float(value.numbers[0])

                if isinstance(value.numbers[1], int) == True :
                    number2 = int(value.numbers[1])
                else:
                    number2 = float(value.numbers[1])

                value.numbers[0] = sum([number1, number2])
                value.numbers.remove(value.numbers[1])
                value.entered_operators.remove(value.entered_operators[0])
            elif value.entered_operators[0] == "-":
                if isinstance(value.numbers[0], int) == True :
                    number1 = int(value.numbers[0])
                else:
                    number1 = float(value.numbers[0])
                    
                if isinstance(value.numbers[1], int) == True :
                    number2 = int(value.numbers[1])
                else:
                    number2 = float(value.numbers[1])
                value.numbers[0] = number1 - number2
                value.numbers.remove(value.numbers[1])
                value.entered_operators.remove(value.entered_operators[0])
            elif value.entered_operators[0] == "%":
                if isinstance(value.numbers[0], int) == True :
                    number1 = int(value.numbers[0])
                else:
                    number1 = float(value.numbers[0])

                if isinstance(value.numbers[1], int) == True :
                    number2 = int(value.numbers[1])
                else:
                    number2 = float(value.numbers[1])

                value.numbers[0] =  number1 % number2
                value.numbers.remove(value.numbers[1])
                value.entered_operators.remove(value.entered_operators[0])
        if len(value.entered_operators) == 0:
            resultValue = value.numbers[0]
            value.entered_operators.clear()
            break
    print("result: ")
    print(value.numbers[0])
    # 
    main.resulttext.set(resultValue)
    # 
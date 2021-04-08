def calc(operator, num1, num2)->float:
    calculaton = 0
    if operator == '+':
        calculaton = num1+num2
        #print('+')
    elif operator == '-':
        calculaton = num1-num2
        #print('-')
    elif operator == 'x':
        calculaton = num1*num2
        #print('x')
    elif operator == '/':
        calculaton = num1/num2
        #print('/')
    elif operator == '^':
        calculaton = num1^num2
        #print('^')
    elif operator == '%':
        calculaton = num1%num2
        #print('%')

    return calculaton

def captureCalculationFromUser()->float:
    calcInput = input('Cal? (+,-,x,/,^,% A B)')
    calcInputList = calcInput.split()
    operator = calcInputList[0]
    num1 = int(calcInputList[1])
    num2 = int(calcInputList[2])
    #print (str(num1) + operator + str(num2) + '=')
    return calc (operator, num1, num2)

def processInstructionsFromFile(filename):
    with open(filename, 'r') as f:
        content = f.readlines()
    calcSum = 0
    #for instruction in content:
    i=0
    while (i<len(content)): 
        instruction = content[i]
        instructionList = instruction.split()
        function = instructionList[0]
        goto = False
        operatorStart = 1
        if function == 'goto':
            goto = True
            if instructionList[1] != 'calc':
                #goto number
                gotoLine = instructionList[1]
                i =gotoLine
            else:
                function = 'calc'
                operatorStart = 2
        else:
            i += 1
        if function == 'calc':
            operator = instructionList[operatorStart]
            num1 = int(instructionList[operatorStart+1])
            num2 = int(instructionList[operatorStart+2])
            calculation = calc (operator, num1, num2)
            #print (str(num1) + operator + str(num2) + '=' + str(calculation))
            calcSum = calcSum + calculation
            #print ("calcSum: " + str(calcSum))

    print ("calcSum: " + str(calcSum))


print(captureCalculationFromUser())
#processInstructionsFromFile('step_2.txt')
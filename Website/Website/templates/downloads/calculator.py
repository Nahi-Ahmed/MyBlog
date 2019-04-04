import sys

print("Calculator")


def calculator():

    ## Asks the user for an input in numbers + operator
    operator = input("Would you like to add, subtract, times or divide?: ")
    operator = operator.lower()

    if operator == "add" or operator == "subtract" or operator == "times" or operator == "divide":
        print("")
    else:
        print("Wrong operator entered! Try again")
        calculator()
        
    number1 = 0
    number2 = 0

    while number1 == 0 and number2 == 0:
        try:
            number1 = float(input("What is the first number?: "))
            number2 = float(input("What is the second?: "))
        except ValueError:
            print("The value entered isn't a number, try again")
            number1 = 0
            number2 = 0
        
    

    
    
    ## Some inputs are converted to a string for ease of file appending later
    strnumber2 = str(number2)
    strnumber1 = str(number1)


    if operator == "add":
        result = number1 + number2
        strresult = str(result)
        print(number1,"+",number2,"=",result)
        final = strnumber1 + " + " + strnumber2 + " = " + strresult

    #Saves the sum in the file below in a new line
        with open("results.txt", "a+") as f:
            f.write(final)
            f.write("\n")
        
    elif operator == "subtract":
        result = number1 - number2
        strresult = str(result)
        print(number1,"-",number2,"=",result)
        final = strnumber1 + " - " + strnumber2 + " = " + strresult

    #Saves the sum in the file below in a new line
        with open("results.txt", "a+") as f:
            f.write(final)
            f.write("\n")
        
    elif operator=="times":
        result = number1 * number2
        strresult = str(result)
        print(number1,"*",number2,"=",result)
        final = strnumber1 + " * " + strnumber2 + " = " + strresult
    
    #Saves the sum in the file below in a new line
        with open("results.txt", "a+") as f:
            f.write(final)
            f.write("\n")
        
    elif operator == "divide":

        if number1 == 0 or number2 == 0:
            result = 0
        else:
            result = number1 / number2

        strresult = str(result)
        print(number1,"/",number2,"=",result)
        final = strnumber1 + " / " + strnumber2 + " = " + strresult
    
    #Saves the sum in the file below in a new line
        with open("results.txt", "a+") as f:
            f.write(final)
            f.write("\n")

    ##Gives the user the choice to restart the program
    restart = input("Would you like to run it again,see history or close the application(run/history/close)?: ")
    restart = restart.lower()
    if restart == "run":
        calculator()
    elif restart == "history":
        with open("results.txt", "r") as f:
            print(f.read())
        restart2 = input("Would you like to run the program again or close the program?(y/n):")
        restart2 = restart2.lower()
        if restart2 == "y":
            calculator()
        elif restart2 == "n":
            sys.exit()
        else:
            print("Wrong value entered")
    else:
        print("Wrong value entered")

##Asks the user to see whether or not the results.txt file should be loaded up
choice = input("Would you like to see previous calculations?(y/n): ")
choice = choice.lower()

if choice == "y":
    with open("results.txt", "r") as f:
        print(f.read())
elif choice == "n":
    calc = input("Would you like to solve a new calculation?(y/n): ")
    calc = calc.lower()
    if calc == "y":
        calculator()
    elif calc == "n":
        sys.exit()
    else:
        print("Wrong value entered")
else:
    print("Wrong value entered")


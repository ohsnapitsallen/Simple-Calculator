#Create a function for the calculator
def calculate():
    print("Let's calculate!")
    #Use try method to ask the user for numbers and operators
    try:
        first = float(input("Enter any number (Can be a whole number or a decimal): "))
        op = str(input('Enter an operator (Must be plus "+", minus "-", times "*", or divide "/": '))
        second = float(input("Enter another number (Can be a whole number or a decimal): "))
        #Use if statements for solving the two numbers depending on the operator that user has inputted
        if op == '+':
                print(first + second)
            elif op == '-':
                print(first - second)
            elif op == '*':
                print(first * second)
            elif op == '/':
                print(first / second)
            else:
                print("Oops! The operator you entered is invalid. Please try again")
    #Create error messages if user's input are invalid or user divides with zero
    except ZeroDivisionError:
        print("You can't divide with zero! (Have you tried dividing 0 cookies you baked among your 0 friends?). Please try again.")
    except ValueError:
        print("Looks like someone doesn't know the difference between their ABCs and 123s (The input is not a number. Please try again.)")
    except:
        print("An unexpected error has occured. Please try again.")
    else:
        break
#Create an empty variable for the while loop to be used later
response = ' '
#Print a welcome message
print("Welcome to Callenculator, created by John Allen Lorena. Please be advised that error messages may be a bit harsh. Use this calculator at your own risk")
#Use the while loop to ask the user if they would like to use the program again
while response != 'no':
    calculate()
    response = str(input('Would you like to try the calculator once more? (Please answer with "yes" or "no" : '))
    #Use if statements depending on the user's response
    if response == 'yes':
        print("Understood.")
    elif response == 'no':
        print("Thank you!")
        break
    else:
        print('The only valid responses are "yes" and "no". Please try again')

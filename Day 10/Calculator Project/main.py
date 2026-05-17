
import art
def add(n1, n2):
    return n1 + n2
#write iut the three ither functions

def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
#add these 4 functions into a dictonary
operations = {
    ""
    "+": add,
    "-": subtract,
    "*": multiply,
    "%": divide
}

#print(operations["*"](4,8))
def calculator():
    print(art.logo)
    should_accumulate = True
    num1 =float(input("what is the first name?:"))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("pick an operation : ")
        num2 = float(input("what is the next number?:"))
        answers=operations[operation_symbol](num1, num2)
        print(f"{num1}{operation_symbol} {num2} ={answers}")
        choice =input(f"Type 'y' to continue calculating with {answers},or type 'n' to start a new calculactions: ")
        if choice == "y":
            num1 = answers
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()
calculator()
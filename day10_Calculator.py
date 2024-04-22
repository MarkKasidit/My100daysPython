
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while True:
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
            
        continued = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to a new calculation: ")
        if continued == 'y':
            num1 = answer
        else:
            calculator()
            break

calculator()
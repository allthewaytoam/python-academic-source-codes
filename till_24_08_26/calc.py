
def calc(a, b, oper):
    match oper:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b if b else "Error: 'Division by zero'"
        case _:
            return "Invalid operator"

def main():
    a = float(input("Enter first number: "))
    oper = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))
    print("Result:", calc(a, b, oper))

if __name__ == "__main__":
    main()

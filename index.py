def main():
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operation (+, -, *, /): ")


    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero")
            return
        else:
            result = num1 / num2
    else:
        print("Invalid operator")
        return

    
    print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()
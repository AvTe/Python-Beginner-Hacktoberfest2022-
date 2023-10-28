import math

def scientific_calculator():
    print("Scientific Calculator")
    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'sub' for subtraction")
        print("Enter 'mul' for multiplication")
        print("Enter 'div' for division")
        print("Enter 'pow' for power/exponentiation")
        print("Enter 'sqrt' for square root")
        print("Enter 'sin' for sine function")
        print("Enter 'cos' for cosine function")
        print("Enter 'tan' for tangent function")
        print("Enter 'log' for natural logarithm")
        print("Enter 'quit' to end the program")
        
        user_input = input(": ")
        
        if user_input == "quit":
            break
        elif user_input == "sqrt":
            num = float(input("Enter a number: "))
            result = math.sqrt(num)
        elif user_input in ("sin", "cos", "tan"):
            angle_deg = float(input("Enter an angle in degrees: "))
            if user_input == "sin":
                result = math.sin(math.radians(angle_deg))
            elif user_input == "cos":
                result = math.cos(math.radians(angle_deg))
            elif user_input == "tan":
                result = math.tan(math.radians(angle_deg))
        elif user_input == "log":
            num = float(input("Enter a number: "))
            result = math.log(num)
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if user_input == "add":
                result = num1 + num2
            elif user_input == "sub":
                result = num1 - num2
            elif user_input == "mul":
                result = num1 * num2
            elif user_input == "div":
                result = num1 / num2
            elif user_input == "pow":
                result = num1 ** num2
            else:
                print("Invalid input")
                continue
        
        print("Result: " + str(result))

if __name__ == "__main__":
    scientific_calculator()

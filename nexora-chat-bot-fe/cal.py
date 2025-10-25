def simple_calculator():
    print("Simple Python Calculator")
    print("------------------------")
    print("Available operations: +, -, *, /")
    
    try:
        # Get user inputs
       
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        
        # Perform calculation based on operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                return 
            result = num1 / num2
        else:
            print("Invalid operation! Please use +, -, *, or /.")
            return 
        
        # Display the result
        print(f"Result: {num1} {operation} {num2} = {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers!")

# Run the calculator
simple_calculator()
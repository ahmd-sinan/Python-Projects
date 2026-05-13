# A simple command-line calculator

def main():
    while True:
        print("----------------CALCULATOR---------------")
        print("[Enter 'q' to Quit]")
        print()

        # Check if user wants to quit
        operator = input("Enter an operator (+, -, *, /): ")
        if operator.lower() == 'q':
            print("Goodbye!")
            break

        # Check if the operator is valid
        if operator not in ['+', '-', '*', '/']:
            print("Invalid Operator!")
            continue
        
        # Get numbers from the user
        try:
            num1 = float(input("Enter 1st number: "))       
            num2 = float(input("Enter 2nd number: "))
        except ValueError:
            print("Error: Please enter valid numbers!")
            continue

        # Perform calculation
        if operator == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")

        elif operator == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")

        elif operator == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")

        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by Zero")
                continue

            result = num1 / num2
            print(f"{num1} / {num2} = {result}")

if __name__ == "__main__":
    main()
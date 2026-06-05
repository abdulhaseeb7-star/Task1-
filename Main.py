def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Simple Calculator")
    print("Enter 'q' at any time to quit.")

    while True:
        op = input("Choose operation (+, -, *, /): ").strip()
        if op.lower() == 'q':
            break
        if op not in ['+', '-', '*', '/']:
            print("Invalid operation. Use +, -, *, or /.")
            continue

        x = get_number("Enter first number: ")
        y = get_number("Enter second number: ")

        try:
            if op == '+':
                result = add(x, y)
            elif op == '-':
                result = subtract(x, y)
            elif op == '*':
                result = multiply(x, y)
            else:
                result = divide(x, y)
            print(f"Result: {result}")
        except ValueError as err:
            print(err)

    print("Calculator closed.")


if __name__ == '__main__':
    main()

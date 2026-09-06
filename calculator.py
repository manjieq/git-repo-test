"""Simple calculator with basic arithmetic operations."""


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


def main():
    ops = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    print("Simple Calculator (Ctrl+C to quit)")
    print("Format: <number> <op> <number>, where op is + - * /")
    while True:
        try:
            expr = input("> ").strip()
            a_str, op, b_str = expr.split()
            result = ops[op](float(a_str), float(b_str))
            print(result)
        except KeyboardInterrupt:
            print("\nBye")
            break
        except (ValueError, KeyError, ZeroDivisionError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

import math_utils

def main():
    try:
        print("Enter first number")
        x = float(input())
        print("Enter second number")
        y = float(input())
        print("Enter operator(+,-,*,/,**,%)")
        op = input().strip()

        if op == '+':
            print(math_utils.add(x, y))
        elif op == '-':
            print(math_utils.subtract(x, y))
        elif op == '*':
            print(math_utils.multiply(x, y))
        elif op == '/':
            print(math_utils.divide(x, y))
        elif op == '**':
            print(math_utils.power(x, y))
        elif op == '%':
            print(math_utils.mod(x, y))
        else:
            print("Invalid operator.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x*y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def power(x, y):
    return x**y

def mod(x, y):
    return x%y

if __name__ == "__main__":
    print("Testing math_utils module functions")
    print("Add Function:", add(3,10 ))
    print("Subtract Function:", subtract(10, 2))
    print("Multiply Function:", multiply(6, 10))
    print("Divide Function:", divide(10, 2))
    print("Divide by zero Condition", divide(20, 0))
    print("Power Function", power(3, 4))
    print("Mod Function:", mod(10, 3))



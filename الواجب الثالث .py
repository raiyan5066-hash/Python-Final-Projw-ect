def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b

num1 = float(input("الرقم الأول: "))
num2 = float(input("الرقم الثاني: "))
op = input("العملية: ")

if op == "+":
    print(add(num1, num2))
elif op == "-":
    print(subtract(num1, num2))
elif op == "*":
    print(multiply(num1, num2))
elif op == "/":
    print(divide(num1, num2))
'''Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication.'''

def num_addition(number1, number2):
    return number1 + number2

def num_subtracion(number1, number2):
    return number1 - number2

def num_division(number1, number2):
    return number1 / number2

def num_multiplication(number1, number2):
    return number1 * number2

number1, number2 = int(input("Please input first number: ")), int(input("Please input second number: "))
print(number1, "+", number2, "=", num_addition(number1, number2))
print(number1, "-", number2, "=", num_subtracion(number1, number2))
print(number1, "/", number2, "=", num_division(number1, number2))
print(number1, "*", number2, "=", num_multiplication(number1, number2))
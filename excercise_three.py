def num_addition(number1, number2):
    sum = number1 + number2
    return sum

def num_subtracion(number1, number2):
    sub = number1 - number2
    return sub

def num_division(number1, number2):
    div = number1 / number2
    return div

def num_multiplication(number1, number2):
    multip = number1 * number2
    return multip

number1, number2 = int(input("Please input first number: ")), int(input("Please input second number: "))
print(f"Sum = {num_addition(number1, number2)}")
print(f"Subtracion = {num_subtracion(number1, number2)}")
print(f"Division = {num_division(number1, number2)}")
print(f"Multiplication = {num_multiplication(number1, number2)}")

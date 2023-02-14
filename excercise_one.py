def names () ->str:
    name, surname = input("Please enter your name: "), input("Please enter your name: ")
    
print(f"Hello ", names())


# def weaker_num(num1, num2):
#     if num1>num2:
#         number = num2
#     else:
#         number = num1
#     return number

# num1, num2 = int(input("Enter first number: ")), int(input("Enter second number: "))

# print(f"Weaker number  = {weaker_num(num1, num2)}")


# import random
# import string

# def generate_random_word(a:int) -> int:
#     alphabet = list(string.ascii_lowercase)
#     return "".join(random.choice(alphabet) for i in range(a))

# print(generate_random_word(10))
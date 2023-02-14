''' Example 1'''
# a = 2
# b = 5

# def addition(number1, number2):
#     sum = number1 + number2
#     return sum

# c = addition(a, b)

# print(c)

'''Example 2'''
# def print_smth():
#     print("Hello world!")

# print_smth()

'''Example 3'''
# import random

# def get_random_number():
#     print(random.randint(0, 10))

# print(get_random_number())

'''Example 4'''
# def find_sum(num1, num2):
#     '''Returns the sum of num1 and num2.'''

#     sum_nums = num1 + num2  # Finds the sum of num1 and num2
#     return sum_nums  # Returns the sum of the numbers

# '''print nothing'''
# find_sum(5, 10) 

# '''prints sum'''
# print(find_sum(5, 10))
# # help(find_sum)
# # print(find_sum.__doc__)

# variable = find_sum(5, 10)
# variable = find_sum(variable, 5)

# print(variable)


'''Example 5'''
# def even_odd(num):

#     '''
#     Returns "even" if num is even, and "odd" if num is odd.    
#     Parameters:
#         num (int): Any integer    Returns:
#         type (string): "even" if num is even; "odd" if num is odd
#     '''

#     if num % 2 == 0:  # Checks if num/2 has a remainder of 0
#         return "even"  # If it has a remainder of 0, return "even"
#     else:
#         return "odd"  # If it doesn't, return "odd"
    
# number = 10

# if even_odd(number) == "even":
#     print(f"My number: {number} is even!")
# else:
#     print(f"My number: {number} is not even")

'''Example 6'''
# def check_if_exist(a=None):
#     if a:
#         return a
    
# a = check_if_exist("A")
# print(a)

'''Example 7'''
# def find_subtraction(num1, num2):
#     '''Returns the sum of num1 and num2.'''

#     sum_nums = num1 + num2  # Finds the sum of num1 and num2
#     return sum_nums  # Returns the sum of the numbers

# print(find_subtraction(5, 50))
# print(find_subtraction(num1=5, num2=50))

'''Example 8'''
# def add_two_int_number(a: int, b:int) -> int:
#     return a + b


# number1 = add_two_int_number(10, 50)

"Example 9"
# type_annotation_int: int = 43
# type_annotation_float: float = 2.54
# type_annotation_string: str = 'efe'
# type_annotation_bool: bool = True

"Example 10"
# from typing import List, Tuple


# Dicttype_annotation_tuple: Tuple[str] = ('1','2','3')
# type_annotation_list: List[str] = ['a', 'b', 'c']
# type_annotation_dict: Dict[str, int] = {'a': 1, 'b': 2}

'''Example 11'''
# def another_fuction(number:int) -> Optinal[int]:
#     if number > 10:
#         return number
#     else:
#         return None
    
# number1:int = another_fuction(1)
# print(number1)
    
'''Example 12'''

# from typing import Tuple, Optional, Union, List

# def the_func(x: Union[int, float], y: Tuple[str, str], z: Optional[float] = None) -> str:
#    return 'You called the_func with ' + str(x) + str(y) + str(z)

# print(the_func(2, ("1", "2")))

'''Example 12'''
# from typing import Tuple, Optional, Union, List

# type_annotation_list: List[float | int]= [1.23, 3.32, 1, 3]
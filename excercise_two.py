'''Create a function that adds a string ending to each member in a list.'''

from typing import List
name_list = ["Tadas", "Mantas", "Mindaugas"]
my_string = ("as")


def string_add(my_list: List[str], my_string: str) -> List[str]:
    str_added = []
    for item in name_list:
        str_added.append(item + my_string)
    return str_added
    

a = string_add(name_list, my_string)
print(a)
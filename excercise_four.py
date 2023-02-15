
'''Create a function that returns only strings with unique characters.'''
from typing import List


strings_list = ["Tomas", "Tadas", "Vytautas", "medis", "Meras","ananasas"]


def unique_values(str_list: List[str])-> List[str]:
    new_str_list = []
    for value in str_list:
        if len(set(value)) == len(value):
            new_str_list.append(value)
            
    return new_str_list


           

unique = unique_values(strings_list)
print(unique)

'''Create a function that returns only strings with unique characters.'''
from typing import List


strings_list = ["Tomas", "Tadas", "Vytautas", "medis", "Meras", "asas"]


def unique_values(str_list: List[str])-> List[str]:
    new_str_list = []
    for value in str_list:
        for i in value:
            if len(set(value)) == len(value):
                new_str_list.append(value)
            
    return set(new_str_list)


           

unique = unique_values(strings_list)
print(unique)
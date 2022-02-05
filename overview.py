# A ordered sequence of multiple values

lists_of_odd_numbers = [1,3,5,7]

# List items can be of any data type

lists_of_strings = ["Two","Four","Six","Eight"]

# All composite data types can store value of any data type, including composite data types

list_of_different_types = ["Two", 1000, 27.0, [1,2,3]]

# 

list_of_odd_numbers = [1,3,5,7]

# Index:

print(list_of_odd_numbers[1])

# Result: The number 3 is printed 

# Python Dictionaries Syntax

# Dictionary Syntax {key: value, key: value, ...}

user_settings = {"lang": "en-us", "platform": "Windows 10"}

member_levels = {1:"Gold", 2:"Silver", 3:"Bronze"}

# Duplicate keys

member_levels = {1:"Gold", 2:"Silver", 3:"Bronze", 3:"Copper"}

# Example: Dictionary order and Indexing 

user_settings = {"lang": "en-us", "platform": "Windows 10"}
print(user_settings["lang"])

# Result: The string "en-us" is printed

# More about Dictionaries
 
orders = {5: "bbq", 2:"tacos", 9:"pizza"}

orders[9] = "tacos"

# Result - The orders variable now contains: 
{5: "bbq", 2:"tacos", 9: "tacos"}

# Python Tuples 

# example
zoo_animals = ("ape", "zebra", "penguin")

# example
empty_tuple = () 

# example:
one_item_tuple = "lion",

zoo_animals = ("ape","zebra","penguin")
zoo_animals = ("elk", "giraffe","condor")

# cannot reasign a value below, only for list 
zoo_animals[0] = "brontosaurus"
zoo_animals.pop(1)

# Python Sets Not
empty_set = {}
empty_set = set() 




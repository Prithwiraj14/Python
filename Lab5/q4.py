# Create a dictionary and apply the following methods
# 1) Print the dictionary items 2) access items 3) use get() 4)change values 5) use len()

my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary:", my_dict)

print("Dictionary items:", my_dict.items())

value_b = my_dict['b']
print("Value of 'b':", value_b)

value_c = my_dict.get('c')
print("Value of 'c' using get():", value_c)

my_dict['c'] = 4
print("Dictionary after changing value of 'c':", my_dict)

dict_length = len(my_dict)
print("Length of dictionary:", dict_length)
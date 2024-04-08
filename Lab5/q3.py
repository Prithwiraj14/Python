# A) Create a tuple and perform the following methods
# 1) Add items 2) len() 3) check for item in tuple 4)Access iems

tup1 = (1, 2, 3, 4, 5, 6)
print("Original Tuple: ", tup1)

tup2 = tup1 + (7, 8)
print('After adding: ', tup2)

if 2 in tup2:
    print("2 is present in the tuple !!")

print("Item at index 4: ", tup2[4])

# B) Write a python program using the following methods: 1) count 2) index
tup3 = (1, 2, 3, 2, 4, 2, 5, 2)
count_2 = tup3.count(2)
print("Counting the value 2: ",count_2)

index_3 = tup3.index(3)
print("Value at index position 3: ", index_3)


# C) Write a python program using “+” and “*” operations which resulting a new tuple?
tuple_a = (1, 2, 3)
tuple_b = (4, 5)
tuple_c = tuple_a + tuple_b
print("Tuple using + operations:", tuple_c)
tuple_d = tuple_b*2
print("After using * operation: ", tuple_d)
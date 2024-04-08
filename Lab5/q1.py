# A) Create a list and perform the following methods
# 1) insert() 2) remove() 3) append() 4) len() 5) pop() 6) clear()

l1 = [1, 2, 3, 4, 5, 6]
print("Original List: ", l1)
l1.insert(2, 4)
print("After insert: ", l1)
l1.remove(2)
print("Removing 2: ", l1)
l1.append(7)
print("Adding 7 at the end: ", l1)

l1_len = len(l1)
print("Length of the list: ", l1_len)

popped_value = l1.pop(2)
print("Popped value", popped_value)
print("List after pop at index 2", l1)

l1.clear()
print("It's cleared !!", l1)

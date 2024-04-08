# Write the code for the following
# The original list : [4, 5, 6]
# The list after alternate repeating elements : [4, 4, 4, 6, 6, 6]

original_list = [4, 5, 6]
result_list = []

for i, num in enumerate(original_list):
    if i % 2 == 0:
        result_list.extend([num] * 3)
    else:
        continue
print("The original list:", original_list)
print("The list after alternate repeating elements:", result_list)
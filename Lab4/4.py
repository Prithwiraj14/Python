# Input : set([12, 10, 13, 15, 8, 9])	Write code
# Output :
# {9, 10, 12, 13, 15}
# {10, 12, 13, 15}
# {12, 13, 15}
# {13, 15}
# {15}
# set()

s = set([12, 10, 13, 15, 8, 9])
sorted_list = sorted(s, reverse=True)

for i in range(len(sorted_list), 0, -1):
    print(set(sorted_list[:i]))

print(set())
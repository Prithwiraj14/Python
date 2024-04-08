s = set([12, 10, 13, 15, 8, 9])
sorted_list = sorted(s, reverse=True)

for i in range(len(sorted_list)):
    print(set(sorted_list[i:]))
print(list(s))
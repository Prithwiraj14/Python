# Input : test_list = [“Gfg”, 3], key_list = [“name”, “id”] 
# Output : [{‘name’: ‘Gfg’, ‘id’: 3}

def create(test, key):
    output = {}
    for i in range(len(key)):
        output[key[i]] = test[i]
    return output
test = ["Gfg", 3]
key = ["name", "id"]
result = create(test, key)
print(result)
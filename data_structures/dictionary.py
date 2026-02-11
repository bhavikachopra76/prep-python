# creating a dictionary
d = {
    "name": "bhavika",
    "age": 20,
    "marks": [85, 90, 78]
}

print(d)  # prints entire dictionary
print(d.items())  # returns all key-value pairs as tuples
print(d.keys())  # returns all keys
print(d.values())  # returns all values

# adding & updating dictionary items
d["city"] = "Mohali"  # adds new key-value pair
d["age"] = 21  # updates existing key
print(d)

# removing elements
d.popitem()  # removes last inserted key-value pair
print(d)

d.pop("marks")  # removes specific key
print(d)

del d["age"]  # deletes key "age"
print(d)

d.clear()  # clears the entire dictionary
print(d)

# another dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)

my_dict.update({'b': 4, 'd': 5})  # updates 'b' and adds new key 'd'
print(my_dict)

# creating a dict with default values
d1 = dict.fromkeys(['e', 'f'], 0)
print(d1)

# safe way to access keys (returns None if not found)
print(my_dict.get('e'))

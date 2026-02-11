# creating a set
my_set = {1,2,3}
print(my_set)  # prints the set (unordered, unique values)

my_set.add(4)
print(my_set)  # adds a single element

my_set.update([5,6,7])
print(my_set)  # adds multiple elements

my_set.remove(7)
print(my_set)  # removes specific element (error if not found)

my_set.clear()
print(my_set)  # clears all elements (becomes empty set)

# set operations
s1 = {'a', 'b', 'c'}
print(s1)

s2 = {'b', 'c', 'd'}
print(s2)

print(s1.union(s2))  # combines elements from both sets
print(s1.intersection(s2))  # common elements
print(s1.difference(s2))  # elements in s1 but not in s2
print(s1.symmetric_difference(s2))  # elements in either set but not both
print(s1.issubset(s2))  # checks if s1 is subset of s2
print(s1.issuperset(s2))  # checks if s1 is superset of s2
print(s1.isdisjoint(s2))  # checks if sets have no common elements
print(3 in s1)  # membership test (False here)

# immutable set
f = frozenset([1,2,3])
print(f)  # like a set but cannot be changed

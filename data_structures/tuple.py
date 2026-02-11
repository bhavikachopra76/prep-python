# working with tuples
# immutable but can contain mutable items
t = (1,2,3)
print(t)  # prints the tuple
print(len(t))  # length of tuple
print(sum(t))  # sum of all elements
print(max(t))  # maximum element
print(min(t))  # minimum element
print(t.count(2))  # counts how many times 2 appears
print(t.index(2))  # finds index of first occurrence of 2

# tuple unpacking
t1 = (4,5,6)
print(t1)  # prints the tuple
a,b,c = t1
print(a,b,c)  # unpacks tuple elements into variables

# parentheses are optional for tuples
t = 1,2,3
print(t)  # same as (1,2,3)

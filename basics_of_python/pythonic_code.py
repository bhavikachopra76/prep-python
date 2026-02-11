#List Comprehension
lst = [1,2,3,4,5,6]
squares = [x*x for x in lst]
print(squares)

even = [x for x in lst if x%2 == 0]
print(even)

even_squares = [x*x for x in lst if x%2 == 0]
print(even_squares)

#Dict Comprehension
lst2 = ["apple" , "banana" , "cherry"]
d = {w : len(w) for w in lst2}
print(d)

#Set Comprehension
nums = [1,2,3,4,5,6,5,6]
square = {n*n for n in nums}
print(square)

#any
lst3 = [1,2,-1,4,5,-8]
flag = any(x < 0 for x in lst3)
print(flag)

#all
lst4 = [1,2,3,4,5,6,-1]
flag2 = all(x<0 for x in lst4)
print(flag2)

#zip
#zip in lists
l1 = [1,2,3,4]
l2 = ['A', 'B', 'C', 'D']
print(list(zip(l1, l2)))

#zip in dictionary
l1 = ["first name", "last name", "age"]
l2 = ["Bhavika", "Chopra", 20]
d = dict(zip(l1, l2))
print(d)

#enumerate
items = ["pen", "pencil", "eraser"]
for i, item in enumerate(items):
    print(i, item)

#zip and enumerate together
items = ["pen", "pencil", "eraser"]
prices = [20, 10, 5]
for i, (item, price) in enumerate(zip(items,prices)):
    print(i, item, price)


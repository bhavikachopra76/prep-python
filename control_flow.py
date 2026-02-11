marks = int(input("Enter marks: "))
if marks > 90:
    print("Excellent")
elif 90> marks > 80:
    print("Awesome")
else:
    print("Good")

print(0 and 5)  # AND -> returns first falsy value (0)
print(1 and 5)  # AND -> returns last value if all are truthy (5)
print(1 or 5)   # OR -> returns first truthy value (1)
print(0 or 5)   # OR -> returns first truthy value (5)
print(not 0)    # NOT -> flips boolean (True)
print(not 1)    # NOT -> flips boolean (False)
print(not 5)    # NOT -> flips boolean (False)

#for loop with list
l = [1,2,3,4]
for value in l:
    print(value)

#for loop with tuple
t = (1,2,3,4)
for val in t:
    print(val)

#for loop with set
s = {1,2,3,4}
for v in s:
    print(v)

#for loop with dictionary
d = {"name" : "Bhavika", "age" : 20}
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
for key, value in d.items():
    print(key, value)

#for loop with range
l = [1,2,3,4]
for i in range(0,3):
    print(i)

#while loop
count = 1
while count <= 5:
    print(count)
    count += 1


l = [1,2,3,4]
print(l)  # prints the whole list
print(l[1:3])  # slicing -> elements from index 1 to 2
print(len(l))  # length of list
print(sum(l))  # sum of all elements
print(max(l))  # maximum element
print(min(l))  # minimum element

l.append(5)
print(l)  # adds 5 at the end

l.insert(1,10)
print(l)  # inserts 10 at index 1

l.extend([20,30])
print(l)  # adds multiple elements at the end

l.remove(10)
print(l)  # removes first occurrence of 10

l.pop()
print(l)  # removes last element

l.pop(1)
print(l)  # removes element at index 1

l.clear()
print(l)  # clears the entire list (becomes [])

# working with another list
nums = [1,25,6,7]
nums.sort()
print(nums)  # sorts in ascending order

nums.sort(reverse=True)
print(nums)  # sorts in descending order

nums.reverse()
print(nums)  # reverses the list

print(nums.index(25))  # returns index of first occurrence of 25
print(nums.count(25))  # counts how many times 25 appears

# Strings in Python are immutable (operations create new strings, not modify originals)
str1 = "Bhavika"

#String slicing

print(str1[0:4])
print(str1[-5:-1])
print(str1[::-1])

#String methods

print(len(str1))
print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.title())
print(str1.replace('B', 'b'))
print(str1.find('B'))

#Join and Split

print('-'.join(['a', 'b', 'c']))

s = "My name is bhavika"
print(s.split())

#String checks methods

print(s.islower())
print(s.isupper())
print(s.count('a'))

#Whitespace handling
s1 = "    my age is 21   "
print(s1.strip())

# Character type check

s2 = '1'
print(s2.isalnum())   # Checks if string is alphanumeric
print(s2.isdigit())   # Checks if string contains only digits
print(s.isalpha())    # Checks if string contains only alphabets
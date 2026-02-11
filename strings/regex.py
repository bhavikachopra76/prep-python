import re  # Import regex module

text = "my age is 21 and i will be 22 next year"

#Digits

print(re.search(r"\d", text)) # Finds first single digit
print(re.search(r"\d+", text)) # Finds first group of consecutive digits
print(re.findall(r"\d+", text)) # Finds all groups of digits

#Word Characters

print(re.search(r"\w", text)) # Finds first word character (letter/digit/_)
print(re.search(r"\w+", text)) # Finds first full word
print(re.findall(r"\w+", text)) # Finds all words

#Whitespace

print(re.findall(r"\s", text)) # Finds all whitespace characters

#Dot(.) Operator

sentence = "the cat sleeps on a cot with a coat"
print(re.search("c.t", sentence)) # Finds first match of c + any char + t
print(re.findall("c.t", sentence)) # Finds all such matches

#Start ^ and End $

text2 = "Hello World"
print(re.search("^Hello", text2)) # Checks if string starts with 'Hello'
print(re.search("World$", text2)) # Checks if string ends with 'World'

#Exact match Quantifiers

phone_number = "1234567890"
print(re.search(r"^\d{10}$", phone_number)) # Validates exact 10-digit number

phone_number = "My phone number is 1234567890"
print(re.search(r"^\d{10}$", phone_number)) # Fails because extra text exists

#Word Boundary

words = "cat scatter catfish"
print(re.search(r"\bcat\b", words)) # Matches 'cat' as a full word only

#Simple Email pattern

email = "testemail@gmail.com"
print(re.search(r"\w+@\w+\.com", email)) # Basic email pattern match

#Grouping and Repetition

print(re.findall("(ab)+", "ab, abb, abbb"))  # Matches repeated 'ab' patterns
print(re.findall("(cat|dog)s?", "i love cats and dog"))  # Matches cat(s) or dog(s)

#re.match

match = "21 is my age"
print(re.match(r"\d+", match)) # Matches because digits are at the start

match = "my age is 21"
print(re.match(r"\d+", match)) # Fails because digits are not at the start

#Substitution

ID = "order id is 1234 backup id is 5678"
print(re.sub(r"\d", "#", ID))  # Replaces every digit with '#'
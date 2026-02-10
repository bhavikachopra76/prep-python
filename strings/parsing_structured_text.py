# Structured text = text that follows a repeated, predictable pattern

row = "Bee, 21, Chandigarh"  # One record (row), comma is the delimiter
print(row)

print(row.split())
# Splits on spaces by default -> ['Bee,', '21,', 'Chandigarh']

#Multi Line Structured Text

text = """Bee,21,Delhi
Alex,22,Mumbai
Sam,20,Pune"""  # Each line represents one row

print(text)

split_text = text.split()
# Splits text into individual rows using whitespace/newlines
print(split_text)

parsed_data = []
for row in split_text:
    columns = row.split(',')   # Split each row into columns using comma
    parsed_data.append(columns)

print(parsed_data)
# Output -> [['Bee', '21', 'Delhi'], ['Alex', '22', 'Mumbai'], ['Sam', '20', 'Pune']]

#Cleaning Dirty Data

rows = [
    " Bee , 21 , Delhi ",
    " Alex , 22 , Mumbai ",
    " Sam , 20 , Pune "
]

parsed_rows = []
for row in rows:
    columns_split = row.split(',')          # Split row into raw columns
    clean_columns = [x.strip() for x in columns_split]
    # strip() removes extra spaces
    parsed_rows.append(clean_columns)

print(parsed_rows)

#Structured Text To Dictionary

info = """name, age, city
Alex, 21, Delhi
Bob, 20, Mumbai
Sam, 24, Bangalore"""
# First row is header, rest are data rows

info_split = info.split("\n")  # Split text by lines

header = info_split[0]         # Extract header row
data = info_split[1:]          # Extract data rows

header_list = header.split(",")  # Convert header into list of keys

parsed_data = []

for row in data:
    clean_columns = [x.strip() for x in row.split(",")]
    # Clean and split each row
    dict_data = dict(zip(header_list, clean_columns))
    # Map headers to values using zip()
    parsed_data.append(dict_data)

print(parsed_data)

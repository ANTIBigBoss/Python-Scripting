# Importing required module
import random

# List examples
grades = [78, 56, 83, 67, 94]
resistor = ['Carbon', 3.9, 5]

# Dynamic list creation
num = []
for i in range(1, 6):
    num += [i]

# List concatenation
n1 = [1, 2, 3, 4, 5]
n2 = [6, 7, 8]
concatenated_list = n1 + n2

# Multi-dimensional lists
matrix = [[6, 2], [5, 9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

# List slicing
company = ['Apple', 'Microsoft', 'Google', 'IBM']
sliced_company = company[1:3]

# List methods
company.remove('Microsoft')
company.append('Oracle')
company.insert(1, 'Yahoo')

# 'in' and 'not in' operators for lists
language = ['C++', 'Java', 'Python', 'Assembly']
if 'Python' in language:
    print('Cool!')
else:
    print('Not cool!')

# Random module usage
binary = ['bit', 'nibble', 'byte', 'word']
chosen_element = random.choice(binary)
random.shuffle(binary)

# Sorting and reversing lists
marks = [78, 92, 56, 85, 67]
marks.sort()
sorted_marks = marks
marks.reverse()
reversed_marks = marks

# Dictionary examples
R = {
    "type": "Carbon",
    "value": 234.56,
    "tol": 10
}

ATmega328 = {
    "type": "AVR microcontroller",
    "word length": 8,
    "clock speed": 16.5,
    "timers": ["Timer0", "Timer1", "Timer2"]
}

# Tuple and set examples
RLC = ('Resistor', 'Capacitor', 'Inductor')
IT = {'Apple', 'Microsoft', 'Google'}

# More dictionary operations
server = {
    "platform": "Linux",
    "Qty": 3,
    "network speed": 2.6,
    "IP address": ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
}
student = {
    "name": "John Doe",
    "id": 2022123,
    "GPA": 3.68
}

# Checking key existence and changing values
if "platform" in server:
    print("\nOperating System is", server["platform"])
server["platform"] = "Windows"

# Adding and removing items
server["status"] = True
removed_status = server.pop("status")

# Looping through dictionaries
for key in server.keys():
    print(key, end=' ')
print()

for value in server.values():
    print(value, end=' ')
print()

for item in server.items():
    print(item, end=' ')
print()

# Printing the results
print("\nConcatenated list:", concatenated_list)
print("\nSliced company list:", sliced_company)
print("\nCompany list after methods:", company)
print("\nChosen element from binary list:", chosen_element)
print("\nShuffled binary list:", binary)
print("\nSorted marks:", sorted_marks)
print("\nReversed marks:", reversed_marks)
print("\nResistor characteristics:", R)
print("\nATmega328 characteristics:", ATmega328)
print("\nRLC tuple:", RLC)
print("\nIT set:", IT)
print("\nServer dictionary after modifications:", server)
print("\nRemoved server status:", removed_status)

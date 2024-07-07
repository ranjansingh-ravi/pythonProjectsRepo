i = 1
result = 1
while i < 20:
    i += 1
    if i % 2 == 0:
        print('Skipping {}'.format(i))
        continue
    print('Multiplying with {}'.format(i))
    result = result * i
print('i:', i)
print('result:', result)

days = ['sun','mon','tue','wed','thu','fri','sat','sun']
for i in days:
    print(i)

for ch in 'Monday':
    print(ch)

# iterating over a dictionary

person = {
    'name' : 'John',
    'Sex' : 'Male',
    'age' : 35,
    "address" : "1945, cincinati"
}

for key in person:
    print('Key is : ', key , " , " , 'Value is : ', person[key])

# to get the values directly

for val in person.values():
    print(val)

# can get both key and value as item

for item in person.items():
    print(item)

# since key and value is tuple we can get them like

for key, val in person.items():
    print('Key is : ', key, " , ", 'Value is : ', val)

# set

set_example_1 = {1, 10}
list_ex = [1,2,2,3,4,5,6,6,9]
# converting list to set
set_example_2 = set(list_ex)
print(set_example_1)
print(set_example_2)

#Union of two sets
print(set_example_2 | set_example_1)

#Intersection of two sets -> present in both set
print(set_example_2 & set_example_1)

#Difference of two sets -> present in first set but not present in second
print(set_example_2 - set_example_1)

#either in set 1 or in set 2 but not present in both
print(set_example_2 ^ set_example_1)

# Using map with a regular function
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# Using map with a lambda function
squared_numbers_lambda = map(lambda x: x * x, numbers)
print(list(squared_numbers_lambda))  # Output: [1, 4, 9, 16, 25]

# Using filter with a regular function
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]

# Using filter with a lambda function
even_numbers_lambda = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers_lambda))  # Output: [2, 4, 6]







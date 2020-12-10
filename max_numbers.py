
numbers = [-2, -1, 0, 1, 2, 3, 4, 5, 6]
factor = 3
positive_numbers = []


# Small Exercise #2
max_number = max(numbers)
print(max_number)

# Small Exercise #3
min_number = min(numbers)
print(min_number)

# Small Exercise #4
for number in numbers:
    if (number % 2) == 0:
        print(number)

# Small Exercise #5
for number in numbers:
    if (number) > 0:
        print(number)

# Small Exercise #6
for number in numbers:
    if (number) > 0:
        positive_numbers.append(number)
print(positive_numbers)

# Small Exercise #7
for number in numbers:
    list = (number * factor)
    print(list)

# Small Exercise #8
numbers.reverse()
print(numbers)
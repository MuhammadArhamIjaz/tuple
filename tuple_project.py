from functools import reduce

# Take input from user
user_input = input("Enter numbers separated by commas (e.g. 2,3,4): ")

# Convert input into a tuple of integers
numbers = tuple(map(int, user_input.split(",")))

# Find the product of tuple elements
product = reduce(lambda x, y: x * y, numbers)

print("Tuple:", numbers)
print("Product of tuple elements:", product)

# Basic Python Concepts

# 1. Variables and Data Types
a = 10
b = 3.14
c = "Hello, Python!"

print("Integer:", a)
print("Float:", b)
print("String:", c)

# 2. Lists and Tuples
my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20, 30, 40, 50)

print("List:", my_list)
print("Tuple:", my_tuple)

# 3. Dictionaries
my_dict = {"name": "John", "age": 25, "city": "New York"}
print("Dictionary:", my_dict)

# 4. Conditional Statements
if a > 5:
    print("a is greater than 5")
else:
    print("a is not greater than 5")

# 5. Loops
# For loop
for i in my_list:
    print("For loop:", i)

# While loop
count = 0
while count < 5:
    print("While loop count:", count)
    count += 1

# 6. Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

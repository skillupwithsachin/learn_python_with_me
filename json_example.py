#Write a program that:
#Prompts the user for their favorite fruit, color, and number.
#Creates a dictionary containing the user's input with the keys: fruit, color, and number.
#Encodes the dictionary into a JSON formatted string.
#Writes the JSON string to a file named "favorites.json".
#Reads the file "favorites.json" and converts the JSON formatted string back into a dictionary.
#Prints the dictionary, mentioning the user's favorite fruit, color, and number in a sentence.

import json

# Function to prompt user for input
def prompt_user_for_input(prompt):
    return input(prompt)

# Prompt user for favorite fruit, color, and number
favorite_fruit = prompt_user_for_input("Enter your favorite fruit: ")
favorite_color = prompt_user_for_input("Enter your favorite color: ")
favorite_number = prompt_user_for_input("Enter your favorite number: ")

# Create dictionary with user's input
favorites_dict = {
    'fruit': favorite_fruit,
    'color': favorite_color,
    'number': favorite_number
}

# Encode dictionary into JSON formatted string
json_str = json.dumps(favorites_dict, indent=4)

# Write JSON string to file "favorites.json"
filename = "favorites.json"
with open(filename, 'w') as f:
    f.write(json_str)
    print(f'JSON data written to {filename}')

# Read JSON string from file "favorites.json" and convert to dictionary
with open(filename, 'r') as f:
    loaded_json_str = f.read()
    loaded_dict = json.loads(loaded_json_str)

# Print dictionary with user's favorites
print("\nUser's favorite details:")
print(f"My favorite fruit is {loaded_dict['fruit']}, my favorite color is {loaded_dict['color']}, and my favorite number is {loaded_dict['number']}.")

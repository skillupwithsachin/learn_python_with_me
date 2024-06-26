# Write a program that sends a POST request to the URL https://httpbin.org/post with a JSON payload.

# The payload should contain a dictionary with three keys: username, password, and email.
# Prompt the user for values for these keys and include them in the payload.
# The program should then display the status code and JSON response.
  
import requests
import json

# Function to prompt user for input
def prompt_user_for_input(prompt):
    return input(prompt)

# URL to send POST request
url = 'https://httpbin.org/post'

# Prompt user for username, password, and email
username = prompt_user_for_input("Enter username: ")
password = prompt_user_for_input("Enter password: ")
email = prompt_user_for_input("Enter email: ")

# Create JSON payload
payload = {
    'username': username,
    'password': password,
    'email': email
}

# Send POST request with JSON payload
try:
    response = requests.post(url, json=payload)
    # Print status code and JSON response
    print(f"Status Code: {response.status_code}")
    print("Response JSON:")
    print(json.dumps(response.json(), indent=4))
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

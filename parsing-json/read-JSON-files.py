import json
import requests

# First, let's create a sample config 
config_data = {
    "api_url": "https://api.example.com/v2",
    "timeout": 30,
    "retry_attempts": 3,
    "enable_logging": True
}

with open('config.json', 'w') as f:
    json.dump(config_data, f, indent=2)


with open('config.json', 'r') as f:
    config = json.load(f)

print(f"API URL: {config['api_url']}")
print(f"Timeout: {config['timeout']} seconds")
print(f"Logging: {'Enabled' if config['enable_logging'] else 'Disabled'}")


# Other real api free avilable apis for practice:

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

for user in users[:3]:  # Show first 3
    print(f"\nName: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"Company: {user['company']['name']}")
    print(f"City: {user['address']['city']}")

# Example 2: Get posts
response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
posts = response.json()

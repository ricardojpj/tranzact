import requests
import json
import random

# Base API URL
base_url = "https://api.realworld.io/api"

# Registration
username = "rp_testapi"+str(random.randint(1,1000))
print("username: ", username)
registration_data = {
    "user": {
        "username": username,
        "email": username+"@gmail.com",
        "password": username
    }
}
response = requests.post(f"{base_url}/users", json=registration_data)
response_data = response.json()
token = response_data["user"]["token"]

# Login
login_data = {
    "user": {
        "email": username+"@gmail.com",
        "password": username
    }
}
response = requests.post(f"{base_url}/users/login", json=login_data)
response_data = response.json()
token = response_data["user"]["token"]

# Headers with the token
headers = {
    "Authorization": f"Token {token}",
    "Content-Type": "application/json"
}

# Create a new Article
article_data = {
    "article": {
        "title": "Test api",
        "description": "Test api",
        "body": "test api",
        "tagList": ["test api"]
    }
}
response = requests.post(f"{base_url}/articles", headers=headers, json=article_data)
article = response.json()["article"]
slug = article["slug"]

# Comment on the article
comment_data = {
    "comment": {
        "body": "comment api"
    }
}
response = requests.post(f"{base_url}/articles/{slug}/comments", headers=headers, json=comment_data)
comment_id = response.json()["comment"]["id"]

# Edit the article
edit_data = {
    "article": {
        "body": "test edit api"
    }
}
response = requests.put(f"{base_url}/articles/{slug}", headers=headers, json=edit_data)

# Delete the comment
response = requests.delete(f"{base_url}/articles/{slug}/comments/{comment_id}", headers=headers)

# Set the article as favorite
response = requests.post(f"{base_url}/articles/{slug}/favorite", headers=headers)

print("Finish API testing")

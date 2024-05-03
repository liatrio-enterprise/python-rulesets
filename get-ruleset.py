import requests
import os

# Replace with your actual token
token = os.environ.get("GITHUB_TOKEN")
base_url = "https://api.github.com"
OWNER = "liatrio-enterprise"
REPO = ""

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}",
    "X-GitHub-Api-Version": "2022-11-28",
}

response = requests.get(f"{base_url}/orgs/{OWNER}/rulesets/713333", headers=headers)

# Print the status code and the response body
print(f"Status code: {response.status_code}")
print(f"Response body: {response.text}")

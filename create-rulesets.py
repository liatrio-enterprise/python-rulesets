import requests
import json
import os

# Define the base URL for the GitHub API
token = os.environ.get("GITHUB_TOKEN")
base_url = "https://api.github.com"
ORG = "liatrio-enterprise"

# Define the headers for the API request
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

def get_rulesets(org):
    response = requests.get(f"{base_url}/orgs/{ORG}/rulesets", headers=headers)
    if response.status_code == 200:
        rulesets = response.json()
        ruleset_dict = {ruleset['name']: ruleset['id'] for ruleset in rulesets}
        print(ruleset_dict)
        return ruleset_dict
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

def main():
    
    # Load the rulesets from the JSON file
    # rulesets = []
    # try:
    #   with open('rulesets.json') as f:
    #     rulesets = json.load(f)
    #     print(rulesets)
    # except Exception as e:
    #  print(f"An error occurred: {e}")
    f = open('rulesets.json')
    data = json.load(f)
    print(data)

    # Iterate through each ruleset
    # for data in rulesets:
    #     # Try to create a new ruleset
    #     create_response = requests.post(f"{base_url}/orgs/{ORG}/rulesets", headers=headers, data=json.dumps(data))
    #     print(create_response.json())

    #     if create_response.status_code == 200:
    #         print("Ruleset created successfully")
    #     elif create_response.status_code == 422 and 'Name must be unique' in str(create_response.json()):
    #         print("Ruleset already exists, exiting...")
    #         exit(1)
    #     else:
    #         print(f"An error occurred: {create_response.json()}")

if __name__ == "__main__":
    main()

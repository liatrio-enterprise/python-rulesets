# This Script will grab information about a ruleset at the org level

import requests
import os

token = os.environ.get("GITHUB_TOKEN")  # Get the token from the environment
base_url = "https://api.github.com" 
ORG = "liatrio-enterprise"              # Name of the organization you want to read the ruleset from
RULESET_NAME = "god mode"         # CHANGE THIS to match the ruleset you created or want to read

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}",
    "X-GitHub-Api-Version": "2022-11-28",
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
    ruleset_dict = get_rulesets(ORG)
    if ruleset_dict is not None:
        RULESET_ID = ruleset_dict.get(RULESET_NAME)
        if RULESET_ID is not None:
            print(f"Ruleset ID: {RULESET_ID}")
            response = requests.get(f"{base_url}/orgs/{ORG}/rulesets/{RULESET_ID}", headers=headers) # This is the endpoint for the ruleset if you have the ruleset ID

            # Print the status code and the response body
            print(f"Status code: {response.status_code}")
            print(f"Response body: {response.text}")
        else:
            print(f"Ruleset {RULESET_NAME} not found")
    else:
        print("No rulesets found")

if __name__ == "__main__":
    main()
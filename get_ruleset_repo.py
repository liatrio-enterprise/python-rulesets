# This Script will grab information about a ruleset at the repo level

import requests
# import os

# TOKEN = os.environ.get("GITHUB_TOKEN")  # Get the token from the environment
# BASE_URL = "https://api.github.com" 
# ORG = "liatrio-enterprise"              # Name of the organization you want to read the ruleset from
# REPO = "all-rules-test"                 # Name of the repository you want to read the ruleset from
# RULESET_NAME = "god mode"         # CHANGE THIS to match the ruleset you created or want to read

# HEADERS = {
#     "Accept": "application/vnd.github+json",
#     "Authorization": f"Bearer {token}",
#     "X-GitHub-Api-Version": "2022-11-28",
# }

def get_rulesets(org, repo, base_url, headers):
    response = requests.get(f"{base_url}/repos/{org}/{repo}/rulesets", headers=headers)
    if response.status_code == 200:
        rulesets = response.json()
        ruleset_dict = {ruleset['name']: ruleset['id'] for ruleset in rulesets}

        # Print Ruleset Dictionary (DEBUGGING)
        print("Rulesets Currently Available:")
        print(ruleset_dict)

        return ruleset_dict
    else:
        print(f"Request failed with status code {response.status_code}")
        return None
    
def main(base_url, headers, org, repo, ruleset_name):
    ruleset_dict = get_rulesets(org, repo, base_url, headers)
    if ruleset_dict is not None:
        ruleset_id = ruleset_dict.get(ruleset_name)
        if ruleset_id is not None:

            # Print Ruleset ID (DEBUGGING)
            # print(f"Ruleset ID: {ruleset_id}")

            # This is the endpoint for the ruleset if you have the ruleset ID
            response = requests.get(f"{base_url}/repos/{org}/{repo}/rulesets/{ruleset_id}", headers=headers)

            # Print the status code and the response body (DEBUGGING)
            # print(f"Status code: {response.status_code}")
            # print(f"Response body: {response.text}")

            return response
        else:
            print(f"Ruleset {ruleset_name} not found")
    else:
        print("No rulesets found")

if __name__ == "__main__":
    main()
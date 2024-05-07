import requests
import json
import os
import logging
import sys

# Set up logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# Define the base URL for the GitHub API
token = os.environ.get("GITHUB_TOKEN")
base_url = "https://api.github.com"
ORG = "liatrio-enterprise"                      #CHANGE THIS VARIABLE TO YOUR ORG NAME
REPO = "python-rulesets"                        #CHANGE THIS VARIABLE TO YOUR REPO NAME
TEAM_RULESET = "team-a-ruleset.json"            #CHANGE THIS VARIABLE TO THE NAME OF YOUR TEAM RULESET FILE
RULESET_TYPE = os.environ.get("RULESET_TYPE")   #Type needs to be `org` or `repo
RULESET_TYPE = "repo"   #Type needs to be `org` or `repo

# Define the headers for the API request
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

def open_file(filename):
    with open(filename, 'r') as f:
        ruleset = json.load(f)
        print(ruleset)
        return ruleset

# Get rulesets ORG
# def get_rulesets(ORG):
#     response = requests.get(f"{base_url}/orgs/{ORG}/rulesets", headers=headers)
#     if response.status_code == 200:
#         rulesets = response.json()
#         ruleset_dict = {ruleset['name']: ruleset['id'] for ruleset in rulesets}
#         print(ruleset_dict)
#         return ruleset_dict
#     else:
#         print(f"Request failed with status code {response.status_code}")
#         return None
    
# Delete rulesets
# def delete_ruleset(ORG):
#   print("Deleting Ruleset")
#   ruleset_dict = get_rulesets(ORG)
#   if ruleset_dict is not None:
#       RULESET_ID = ruleset_dict.get(rulesets['name'])
#       if RULESET_ID is not None:
#           delete_response = requests.delete(f"{base_url}/orgs/{ORG}/rulesets/{RULESET_ID}", headers=headers)
#           if delete_response.status_code == 204:
#               print("Ruleset deleted successfully")
#           else:
#               print(f"Failed to delete ruleset: {delete_response.json()}")
#       else:
#           print("Ruleset not found")

def create_ruleset_org(ORG, ruleset):
    print("Creating Ruleset for ORG")
    try:
        # Make the POST request, passing the ruleset as the data
        create_response = requests.post(f"{base_url}/orgs/{ORG}/rulesets", headers=headers, data=json.dumps(ruleset))
        create_response.raise_for_status()  # Raises a HTTPError if the status code is 4xx or 5xx
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
    else:
        print("Response status code:", create_response.status_code)
        print("Response headers:", create_response.headers)
        if 'application/json' in create_response.headers.get('Content-Type'):
            print("Response body:", json.dumps(create_response.json(), indent=4))
        else:
            print("Response body:", create_response.text)

def create_ruleset_repo(REPO, ORG, ruleset):
    print("Creating Ruleset for REPO")
    try:
        # Make the POST request, passing the ruleset as the data
        create_response = requests.post(f"{base_url}/repos/{ORG}/{REPO}/rulesets", headers=headers, data=json.dumps(ruleset))
        create_response.raise_for_status()  # Raises a HTTPError if the status code is 4xx or 5xx
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
    else:
        print("Response status code:", create_response.status_code)
        print("Response headers:", create_response.headers)
        if 'application/json' in create_response.headers.get('Content-Type'):
            print("Response body:", json.dumps(create_response.json(), indent=4))
        else:
            print("Response body:", create_response.text)

def main():
    # if os.environ.get("DELETE_RULESET") == "true":
    #   delete_ruleset(ORG)

    print(f"RULESET_TYPE: {RULESET_TYPE}")

    if RULESET_TYPE == "org":
        ruleset = open_file('org_ruleset.json')
        print("opened org_ruleset.json")
    elif RULESET_TYPE == "repo":
        filepath = f'teams_rulesets/{TEAM_RULESET}'
        print(f"filepath: {filepath}")
        ruleset = open_file(filepath)
        print(f"opened teams_rulesets/{TEAM_RULESET}")
    else:
        print("No action specified, please set RULESET_TYPE as an environment variable. Expected Values are 'org' and 'repo'")
        sys.exit(1)
        

    # for ruleset in rulesets:
    if RULESET_TYPE == "org":
        create_ruleset_org(ORG, ruleset)
    elif RULESET_TYPE == "repo":
        create_ruleset_repo(REPO, ORG, ruleset)
    else:
        print("No action specified, please set RULESET_TYPE as an environment variable. Expected Values are 'org' and 'repo'")
        sys.exit(1)
        # create_ruleset_org(ORG, ruleset)

#   for ruleset in rulesets:
#       try:
#           # Make the POST request, passing the ruleset as the data
#           create_response = requests.post(f"{base_url}/orgs/{ORG}/rulesets", headers=headers, data=json.dumps(ruleset))
#           create_response.raise_for_status()  # Raises a HTTPError if the status code is 4xx or 5xx
#       except requests.exceptions.HTTPError as err:
#           print(f"HTTP error occurred: {err}")
#       except requests.exceptions.RequestException as err:
#           print(f"Other error occurred: {err}")
#       else:
#           print("Response status code:", create_response.status_code)
#           print("Response headers:", create_response.headers)
#           if 'application/json' in create_response.headers.get('Content-Type'):
#               print("Response body:", json.dumps(create_response.json(), indent=4))
#           else:
#               print("Response body:", create_response.text)   

if __name__ == "__main__":
    main()

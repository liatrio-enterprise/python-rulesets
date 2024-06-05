# This script will create a ruleset at the org level only, based on the given parameters
# Rulset Manifest MUST be wrapped in a list object in json, otherwise this script WILL NOT work

import requests
import json
import os
import logging

# Set up logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# Define the base URL for the GitHub API
TOKEN = os.environ.get("GITHUB_TOKEN")      # Get the token from the environment
BASE_URL = "https://api.github.com"         # Base URL for the GitHub API
ORG = "liatrio-enterprise"                  # CHANGE THIS VARIABLE TO YOUR ORG NAME
FILE_NAME = "new_manifest_example.json"     # CHANGE THIS VARIABLE TO THE NAME OF YOUR MANIFEST FILE
FILE_PATH = f"manifest/new/{FILE_NAME}"     # CHANGE THIS VARIABLE TO THE PATH OF YOUR MANIFEST FILE
# team_name = os.getenv('TEAM_NAME')
# if team_name:
#     file_name = f'teams_ruleset/team_{team_name}.json'
# else:
#     file_name = 'teams_rulesets/base_ruleset.json'

# Define the headers for the API request
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

# Define the data for the new ruleset
with open(FILE_PATH, 'r') as f:
    rulesets = json.load(f)
    print(rulesets)

# Get rulesets
def get_rulesets(ORG):
    response = requests.get(f"{BASE_URL}/orgs/{ORG}/rulesets", headers=headers)
    if response.status_code == 200:
        rulesets = response.json()
        ruleset_dict = {ruleset['name']: ruleset['id'] for ruleset in rulesets}
        print(ruleset_dict)
        return ruleset_dict
    else:
        print(f"Request failed with status code {response.status_code}")
        return None
    
# Delete rulesets
# def delete_ruleset(ORG):
#   print("Deleting Ruleset")
#   ruleset_dict = get_rulesets(ORG)
#   if ruleset_dict is not None:
#       RULESET_ID = ruleset_dict.get(rulesets['name'])
#       if RULESET_ID is not None:
#           delete_response = requests.delete(f"{BASE_URL}/orgs/{ORG}/rulesets/{RULESET_ID}", headers=headers)
#           if delete_response.status_code == 204:
#               print("Ruleset deleted successfully")
#           else:
#               print(f"Failed to delete ruleset: {delete_response.json()}")
#       else:
#           print("Ruleset not found")

def main():
  # if os.environ.get("DELETE_RULESET") == "true":
  #   delete_ruleset(ORG)
  for ruleset in rulesets:
      try:
          # Make the POST request, passing the ruleset as the data
          create_response = requests.post(f"{BASE_URL}/orgs/{ORG}/rulesets", headers=headers, data=json.dumps(ruleset))
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

if __name__ == "__main__":
    main()

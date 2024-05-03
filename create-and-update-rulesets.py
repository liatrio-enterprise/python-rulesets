import requests
import json
import os

# Define the base URL for the GitHub API
token = os.environ.get("GITHUB_TOKEN")
base_url = "https://api.github.com"
ORG = "liatrio-clients" #CHANGE THIS VARIABLE TO YOUR ORG NAME

# Define the headers for the API request
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

# Define the data for the ruleset
data = {
    "org": ORG,
    "name": "Python Ruleset",
    "target": "branch",
    "enforcement": "active",
    "conditions": {
        "ref_name": {
            "include": ["~DEFAULT_BRANCH"],
            "exclude": []
        },
        "repository_property": {
            "include": [
                {
                    "name": "Ownership",
                    "property_values": ["github_practice"]
                },
                {
                    "name": "RepositoryType",
                    "property_values": ["automation"]
                }
            ],
            "exclude": []
        },
    },
    "rules": [
        {
            "type": "required_status_checks",
            "parameters": {
                "strict_required_status_checks_policy": False,
                "required_status_checks": [
                    {
                        "context": "CodeQL"
                    }
                ]
            },
        },
        {
            "type": "pull_request",
            "parameters": {
                "dismiss_stale_reviews_on_push": False,
                "require_code_owner_review": False,
                "require_last_push_approval": True,
                "required_approving_review_count": 1,
                "required_review_thread_resolution": True
            }
        },
    ],
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
  deleteFlag = False
  # Try to create a new ruleset
  create_response = requests.post(f"{base_url}/orgs/{ORG}/rulesets", headers=headers, data=json.dumps(data))
  print(create_response.json())

  # Check Delete Variable
  if os.environ.get("DELETE_FLAG") == "True": # Assign environment variable DELETE_FLAG to delete ruleset
    deleteFlag = True

  if deleteFlag == True:
    print("Deleting Ruleset")
    ruleset_dict = get_rulesets(ORG)
    if ruleset_dict is not None:
        RULESET_ID = ruleset_dict.get(data['name'])
        if RULESET_ID is not None:
            delete_response = requests.delete(f"{base_url}/orgs/{ORG}/rulesets/{RULESET_ID}", headers=headers)
            if delete_response.status_code == 204:
                print("Ruleset deleted successfully")
            else:
                print(f"Failed to delete ruleset: {delete_response.json()}")
        else:
            print("Ruleset not found")
  elif create_response.status_code == 200:
      print("Ruleset created successfully")
  elif create_response.status_code == 422 and 'Name must be unique' in str(create_response.json()):
      print("Ruleset already exists, updating...")
      # If the ruleset already exists, update it
      ruleset_dict = get_rulesets(ORG)
      if ruleset_dict is not None:
          RULESET_ID = ruleset_dict.get(data['name'])
          if RULESET_ID is not None:
              update_response = requests.put(f"{base_url}/orgs/{ORG}/rulesets/{RULESET_ID}", headers=headers, data=json.dumps(data))
              if update_response.status_code == 200:
                  print("Ruleset updated successfully")
              else:
                  print(f"Failed to update ruleset: {update_response.json()}")
          else:
              print("Ruleset not found")
  else:
      print(f"An error occurred: {create_response.json()}")

if __name__ == "__main__":
    main()

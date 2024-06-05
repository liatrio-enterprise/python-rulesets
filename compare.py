import get_ruleset_repo
import get_ruleset_org
import os
import json
import sys

TOKEN = os.environ.get("AUTH_TOKEN")  # Get the token from the environment
TYPE = os.environ.get("TYPE")           # Get the type from the environment
BASE_URL = "https://api.github.com"     # Base URL for the GitHub API

# If using locally, uncomment the following lines and comment out the os.environ.get lines
# ORG = "liatrio-enterprise"              # Name of the organization you want to read the ruleset from
# REPO = "all-rules-test"                 # Name of the repository you want to read the ruleset from
# RULESET_NAME = "Base Manifest"          # CHANGE THIS to match the ruleset you created or want to read
# MANIFEST_FILE_NAME = "base.json"        # CHANGE THIS to match the manifest file you want to compare to 

# If using in a workflow, uncomment the following lines and comment out the above lines
ORG = os.environ.get("ORG")                                 # Name of the organization you want to read the ruleset from
REPO = os.environ.get("REPO")                               # Name of the repository you want to read the ruleset from
RULESET_NAME = os.environ.get("RULESET_NAME")               # CHANGE THIS to match the ruleset you created or want to read
MANIFEST_FILE_NAME = os.environ.get("MANIFEST_FILE_NAME")   # CHANGE THIS to match the manifest file you want to compare to 

# Headers for the GitHub API
HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28",
}

def main():
    print("Hello from main")
    print("Here are the environement variables being read")
    print(TOKEN)
    print(TYPE)
    print(ORG)
    print(REPO)
    print(RULESET_NAME)
    print(MANIFEST_FILE_NAME)
    if TYPE == "org":
        # print("I am here checking org ruleset match")
        responseORG = get_ruleset_org.main(BASE_URL, HEADERS, ORG, RULESET_NAME)
        # print(responseORG.text)
        with open(f"manifest/org/{MANIFEST_FILE_NAME}", 'r') as file:
            manifest_data = json.load(file)
        response_data = json.loads(responseORG.text)

        if manifest_data == response_data:
            print("The response matches with the manifest file.")
            sys.exit(0)  # Exit with code 0 (good)
        else:
            print("The response does not match with the manifest file.")
            sys.exit(1)  # Exit with code 1 (bad)
    elif TYPE == "repo":
        # print("I am here checking repo ruleset match")
        responseREPO = get_ruleset_repo.main(BASE_URL, HEADERS, ORG, REPO, RULESET_NAME)
        # print(responseREPO.text)
        with open(f"manifest/repo/{MANIFEST_FILE_NAME}", 'r') as file:
            manifest_data = json.load(file)
        response_data = json.loads(responseREPO.text)
        if manifest_data == response_data:
            print("The response matches with the manifest file.")
            sys.exit(0)  # Exit with code 0 (good)
        else:
            print("The response does not match with the manifest file.")
            sys.exit(1)  # Exit with code 1 (bad)
    else:
        print("Invalid type. Please specify either 'org' or 'repo'")

if __name__ == "__main__":
    main()
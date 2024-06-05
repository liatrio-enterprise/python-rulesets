import get_ruleset_repo
import get_ruleset_org
import os
import json
import sys

# This Script will verify if the ruleset is present at the org or repo level

# These Global Variables are used for the workflow
TOKEN = os.environ.get("GITHUB_TOKEN")  # Get the token from the environment
BASE_URL = "https://api.github.com" 
# ORG = "liatrio-enterprise"              # Name of the organization you want to read the ruleset from
# REPO = "all-rules-test"                 # Name of the repository you want to read the ruleset from
# RULESET_NAME = "Base Manifest"          # CHANGE THIS to match the ruleset you created or want to read
# MANIFEST_FILE_NAME = "base.json"        # CHANGE THIS to match the manifest file you created or want to read

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28",
}

def main():

    print("1.) Grab New Ruleset Manifest from Github Enterprise/Server and save file locally (ORG)")
    print("2.) Grab New Ruleset Manifest from Github Enterprise/Server and save file locally (REPO)")
    print("3.) Grab Latest Ruleset Manifest from Github Enterprise/Server and update file locally (ORG)")
    print("4.) Grab Latest Ruleset Manifest from Github Enterprise/Server and update file locally (REPO)")
    user_input = input("Please enter a selection: ")

    if user_input == "1":
        print("Grabbing New Ruleset Manifest from Github Enterprise/Server and saving file locally (ORG)")
        print("What is the name of the org you want to grab the ruleset from?")
        user_input = input("Please enter the org name: ")
        org = user_input
        print("What is the name of the ruleset you want to grab?")
        user_input = input("Please enter the ruleset name: ")
        ruleset_name = user_input
        print("What is the name of the file you want to save the ruleset to?")
        user_input = input("Please enter the manifest name: ")
        manifest_file_name_save = user_input
        responseORG = get_ruleset_org.main(BASE_URL, HEADERS, org, ruleset_name)
        if responseORG is not None:
            # Convert the response to JSON
            responseORG_json = responseORG.text
            json_data = json.loads(responseORG_json)

            # Write the JSON data to a file
            with open(f"./manifest/save/{manifest_file_name_save}.json", 'w') as json_file:
                json.dump(json_data, json_file)
        else:
            print("No response found.")

    elif user_input == "2":
        print("Grabbing New Ruleset Manifest from Github Enterprise/Server and saving file locally (REPO)")
        print("What is the name of the org you want to grab the ruleset from?")
        user_input = input("Please enter the org name: ")
        org = user_input
        print("What is the name of the repo you want to grab the ruleset from?")
        user_input = input("Please enter the repo name: ")
        repo = user_input
        print("What is the name of the ruleset you want to grab?")
        user_input = input("Please enter the ruleset name: ")
        ruleset_name = user_input
        print("What is the name of the file you want to save the ruleset to?")
        user_input = input("Please enter the manifest name: ")
        manifest_file_name_save = user_input
        responseREPO = get_ruleset_repo.main(BASE_URL, HEADERS, org, repo, ruleset_name)
        if responseREPO is not None:
            # Convert the response to JSON
            responseREPO_json = responseREPO.text
            json_data = json.loads(responseREPO_json)

            # Write the JSON data to a file
            with open(f"./manifest/save/{manifest_file_name_save}.json", 'w') as json_file:
                json.dump(json_data, json_file)
        else:
            print("No response found.")

    elif user_input == "3":
        print("Grabbing Latest Ruleset Manifest from Github Enterprise/Server and updating file locally (ORG)")
        print("What is the name of the org you want to grab the ruleset from?")
        user_input = input("Please enter the org name: ")
        org = user_input
        print("What is the name of the ruleset you want to update?")
        user_input = input("Please enter the ruleset name: ")
        ruleset_name = user_input
        print("What is the name of the file you want to update the ruleset to?")
        user_input = input("Please enter the manifest name: ")
        manifest_file_name = user_input
        responseORG = get_ruleset_org.main(BASE_URL, HEADERS, org, ruleset_name)
        if responseORG is not None:
            # Convert the response to JSON
            responseORG_json = responseORG.text
            json_data = json.loads(responseORG_json)

            # Write the JSON data to a file
            with open(f"./manifest/org/{manifest_file_name}.json", 'w') as json_file:
                json.dump(json_data, json_file)
        else:
            print("No response found.")

    elif user_input == "4":
        print("Grabbing Latest Ruleset Manifest from Github Enterprise/Server and updating file locally (REPO)")
        print("What is the name of the org you want to grab the ruleset from?")
        user_input = input("Please enter the org name: ")
        org = user_input
        print("What is the name of the repo you want to grab the ruleset from?")
        user_input = input("Please enter the repo name: ")
        repo = user_input
        print("What is the name of the ruleset you want to update?")
        user_input = input("Please enter the ruleset name: ")
        ruleset_name = user_input
        print("What is the name of the file you want to update the ruleset to?")
        user_input = input("Please enter the manifest name: ")
        manifest_file_name = user_input
        responseREPO = get_ruleset_repo.main(BASE_URL, HEADERS, org, repo, ruleset_name)
        if responseREPO is not None:
            # Convert the response to JSON
            responseREPO_json = responseREPO.text
            json_data = json.loads(responseREPO_json)

            # Write the JSON data to a file
            with open(f"./manifest/repo/{manifest_file_name}.json", 'w') as json_file:
                json.dump(json_data, json_file)
        else:
            print("No response found.")

    else:
        print("Invalid selection. Please select a number from the list.")

if __name__ == "__main__":
    main()
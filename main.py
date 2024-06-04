import get_ruleset_repo
import get_ruleset_org
import os
import json
import sys

# This Script will verify if the ruleset is present at the org or repo level

# These Global Variables are used for the workflow
TOKEN = os.environ.get("GITHUB_TOKEN")  # Get the token from the environment
BASE_URL = "https://api.github.com" 
ORG = "liatrio-enterprise"              # Name of the organization you want to read the ruleset from
REPO = "all-rules-test"                 # Name of the repository you want to read the ruleset from
RULESET_NAME = "Base Manifest"          # CHANGE THIS to match the ruleset you created or want to read
MANIFEST_FILE_NAME = "base.json"        # CHANGE THIS to match the manifest file you created or want to read

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28",
}

# KEYS_TO_IGNORE = ['node_id', 'created_at', 'updated_at']

# def remove_keys(obj, rubbish):
#     """
#     This function removes the specified keys from a dictionary.
#     """
#     if isinstance(obj, dict):
#         obj = {
#             key: remove_keys(value, rubbish)
#             for key, value in obj.items()
#             if key not in rubbish
#         }
#     elif isinstance(obj, list):
#         obj = [remove_keys(item, rubbish) for item in obj]
#     return obj

# def compare_rules(base_rules, second_rules):
#     # Convert each dictionary in the list to a frozenset, which is hashable and can be put in a set
#     base_rules_set = set(frozenset(rule.items()) for rule in base_rules)
#     second_rules_set = set(frozenset(rule.items()) for rule in second_rules)

#     # Compare the sets
#     return base_rules_set == second_rules_set

def main():

    print("1.) Grab New Ruleset Manifest from Github Enterprise/Server and save file locally (ORG)")
    print("2.) Grab New Ruleset Manifest from Github Enterprise/Server and save file locally (REPO)")
    print("3.) Grab Latest Ruleset Manifest from Github Enterprise/Server and update file locally (ORG)")
    print("4.) Grab Latest Ruleset Manifest from Github Enterprise/Server and update file locally (REPO)")
    print("5.) Compare Ruleset Manifest from Github Enterprise/Server with local file")
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

    elif user_input == "5":
        print("Comparing Ruleset Manifest from Github Enterprise/Server with local file")
        print("What is the type of ruleset you want to compare? (org/repo)")
        user_input = input("Please enter a selection: ")
        type = user_input
        if type == "org":
            # print("I am here checking org ruleset match")
            responseORG = get_ruleset_org.main(BASE_URL, HEADERS, ORG, RULESET_NAME)
            # print(responseORG.text)
            with open(f"manifest/org/{MANIFEST_FILE_NAME}", 'r') as file:
                manifest_data = json.load(file)
            response_data = json.loads(responseORG.text)

            # filter out keys that are not needed for comparison
            # manifest_data_filtered = remove_keys(manifest_data, KEYS_TO_IGNORE)
            # response_data_filtered = remove_keys(response_data, KEYS_TO_IGNORE)

            # print filtered data (DEBUGGING)
            # print(manifest_data_filtered)
            # print(response_data_filtered)

            # compare the filtered data fist before the rules
            # for key in manifest_data_filtered:
            #     if key not in response_data_filtered or manifest_data_filtered[key] != response_data_filtered[key]:
            #         print("The response does not match with the manifest file.")
            #         sys.exit(1)  # Exit with code 1 (bad)
            #         # return False

            # base_rules = manifest_data['rules']
            # second_rules = response_data['rules']

            # Check if the 'rules' lists match
            # if compare_rules(base_rules, second_rules):
            #     print("The 'rules' lists match.")
            # else:
            #     print("The 'rules' lists do not match.")
            #     print("The response matches with the manifest file.")
            #     sys.exit(0)

            if manifest_data == response_data:
                print("The response matches with the manifest file.")
                sys.exit(0)  # Exit with code 0 (good)
            else:
                print("The response does not match with the manifest file.")
                sys.exit(1)  # Exit with code 1 (bad)
        elif type == "repo":
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

    else:
        print("Invalid selection. Please select a number from the list.")

if __name__ == "__main__":
    main()
# python-rulesets

GitHub Actions workflow for creating organization level rulesets.

## Usage

This Python script will either create a *base* ruleset or a *team* ruleset at the organization level.

To start, generate a Personal Access Token with *admin:org* access and save this token as a repository secret named *GH_TOKEN*.

### Base Ruleset

To create a base ruleset, simply trigger the workflow manually in the Actions tab without providing any inputs.

### Team Ruleset

To create a team ruleset, add a new JSON file in the teams_rulesets/ directory and provide the information required for the ruleset you want to generate. You can take a look at the other JSON files to follow the schema. The name of your file should follow the syntax: team_< your_team_name >.json.

Once this file is created, head over to the Actions tab and provide the team name as an input to the workflow.

Ex. If your file is called "team_a.json", simply provide "a" as an input.

## Local

To test locally, make sure to set the *GITHUB_TOKEN* and *TEAM_NAME* environment variable, where *GITHUB_TOKEN* is a personal access token with *admin:org* access and *TEAM_NAME* is the name of the team corresponding to the JSON configuration that you want to apply.

Also make sure to install the Python dependencies in requirements.txt.

## Schema

To understand the format of the JSON file for creating rulesets, you can use the *get-ruleset-org.py* script to pull down an existing ruleset.
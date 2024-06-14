# python-rulesets

Scripts for managing, creating and enforcing Github Enterprise Cloud Rulesets

## Usage

This Repository contains several different scripts

Also make sure to install the Python dependencies in requirements.txt.

- `compare.py`
- `create_rulesests.py`
- `get_ruleset_org.py`
- `get_ruleset_repo.py`
- `local_dev.py`

all of which do different things listed below

### Comparing Manifest (Workflow)

`compare.py`

This script imports a few environment varibales to be used by the script:

- `AUTH_TOKEN`: Github Token provided by secrets
- `TYPE`: specified as `org` or `repo` depending on what is being tested
- `ORG`: org name to compare manifest to
- `REPO`: repo name to comapre manifest to
- `RULESET_NAME`: name of ruleset to compare
- `MANIFEST_FILE_NAME`: name of manifest file (not inclusing `.json` extension)

The script will use this information and make a comparison to the current manifest that exist locally in the repository. If it doesn't match
what is on the backend, the workflow will fail and return with error code 1.

To run the script locally, install the requirements from `requirements.txt` files and run `python compare.py`

Reference workflow `check_manifest.yml` for workflow application.

### Creating Rulesets (Local)

`create_rulesets.py`

This script uses the following variables:

- `TOKEN`: Github Token provided by environment variable
- `ORG`: org name for location to make ruleset
- `FILE_NAME`: file name of manifest to use to create new ruleset
- `FILE_PATH`: file path, which includes `FILE_NAME`, where manifest is located

This script will create a new ruleset at the org level using a manifest file created by a user locally. `create_rulesets.py` will use the default path of `manifests/new` to creeate new rulesets. 

To run the script, install the requirements from `requirements.txt` files and run `python create_rulesets.py`

There are example manifest files located in the `examples` folder under the `manifests` folder. Use these as a guide to create new custom manifests.

You can also reference the [REST API Documentation](https://docs.github.com/en/rest?apiVersion=2022-11-28) to get a better understading of what options there are.

### Gathering and Updating Manifest (Local)

`local_dev.py`

This script uses a Terminal User Interface to do the following:

1. Create new manifest copy for an org/repo

Script will download a new copy of an existing manifest to be checked for changes, the new manifest files will be saved to the `manifest/save` folder by default and will need to be moved/added to the `manifest/(org/repo)` directory to be enforced later after pushed to repo.

2. Update manifest copy for org/repo

Script will update an existing copy of a manifest so that the new manifest can be referenced if changes were made. These will also be saved to the `manifest/save` directory and will need to be moved to the according location to be enforced on next push.

Information will need to be entered after a selection is made. For example:

Selection 1 will create a new copy of a manifest from GitHub, this will require an `ORG` name, a `RULESET_NAME`, and a `MANIFEST_FILE_NAME` (not including the `.json` extension). This information will need to be entered manually after making the selection, and will not be imported from an already exisiting variable.

The remaining scripts:

`get_ruleset_org.py`
`get_ruleset_repo.py`

These files are used by `local_dev.py` to gather data about the ruleset that you are trying to grab or update. Functions in these files use arguments provided
by the `local_dev.py` script.

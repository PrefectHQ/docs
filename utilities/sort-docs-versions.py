import argparse
import json

from packaging.version import parse as parseVersion

def get_versions_json(file_path):
    """Accepts a file path for versions.json and returns a dict containing
    the versions JSON file.

    Args:
        file_path (str): A file path for versions.json

    Returns:
        list: A list of dicts containing version information
    """
    with open(file_path, "r") as f:
        return json.load(f)


def sort_versions_json(versions_json):
    """Accepts a list containing versions json dicts and sorts the
    versions in descending order.

    Args:
        versions_json (list): A list of dicts containing version information
    Returns:
        dict: A dict containing the versions JSON file with sorted versions
    """
    # use sorted() to sort the versions in descending order
    sorted_versions = sorted(
        versions_json,
        key=lambda version: parseVersion(version["version"]),
        reverse=True,
    )

    # iterate over the sorted versions and set the "aliases" key to an empty list
    for version in sorted_versions:
        version["aliases"] = []

    # then, add the "latest" alias to the first version
    sorted_versions[0]["aliases"].append("latest")

    return sorted_versions


def save_versions_json(versions_json, file_path):
    """Accepts a list containing versions json dicts and a file path for
    the versions json file and saves it to a JSON file.

    Args:
        versions_json (list): A list of dicts containing version information
        file_path (str): A file path for the versions json file
    """
    with open(file_path, "w") as f:
        json.dump(versions_json, f, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--versions-file-path",
        help="The path to the versions.json file",
    )

    args = parser.parse_args()

    versions_json = get_versions_json(args.versions_file_path)
    sorted_versions = sort_versions_json(versions_json)
    save_versions_json(sorted_versions, args.versions_file_path)

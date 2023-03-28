import argparse

import tomlkit


def get_netlify_config(file_path):
    """Accepts a file path for netlify.toml and returns a dict containing
    the Netlify config.

    Args:
        file_path (str): A file path for netlify.toml

    Returns:
        dict: A dict containing the Netlify config
    """
    with open(file_path, "r") as f:
        return tomlkit.parse(f.read())
    

def update_netlify_config_with_overrides(netlify_config, file_path):
    """Accepts a dict containing the netlify config and a file path for
    netlify.overrides.toml and updates the netlify config dict with the
    values from the overrides file. If the key already exists in the
    Netlify config dict, it is overwritten with the value from the
    overrides file.
    
    Args:
        netlify_config (dict): A dict containing the Netlify config
        file_path (str): A file path for overrides to the Netlify config
    """
    with open(file_path, "r") as f:
        overrides = tomlkit.parse(f.read())
    for key in overrides:
        netlify_config[key] = overrides[key]


def update_netlify_config_with_additions(netlify_config, file_path):
    """Accepts a dict containing the Netlify config and a file path for
    netlify.additions.toml and updates the netlify config dict with the
    values from the additions file. If the key already exists in the
    Netlify config dict, the value from the additions file is appended to
    the value in the netlify config dict.
    
    Args:
        netlify_config (dict): A dict containing the netlify config
        file_path (str): A file path for additions to the netlify config"""
    with open(file_path, "r") as f:
        additions = tomlkit.parse(f.read())
    for key in additions:
        if key in netlify_config:
            netlify_config[key] += additions[key]
        else:
            netlify_config[key] = additions[key]


# A function that saves the Netlify config dict to a TOML file.
def save_netlify_config(netlify_config, file_path):
    """Accepts a dict containing the Netlify config and a file path for
    the Netlify config and saves it to a TOML file.

    Args:
        netlify_config (dict): A dict containing the Netlify config
        file_path (str): A file path for the Netlify config
    """
    with open(file_path, "w") as f:
        f.write(tomlkit.dumps(netlify_config))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-config-path",
        type=str,
        default=None,
        help="The path to the original Netlify config file",
        required=True
    )
    parser.add_argument(
        "--overrides-path",
        type=str,
        default=None,
        help="The path to the Netlify overrides file",
        required=True
    )
    parser.add_argument(
        "--additions-path",
        type=str,
        default=None,
        help="The path to the Netlify additions file",
        required=True
    )
    parser.add_argument(
        "--output-config-path",
        type=str,
        default=None,
        help="The path to the output Netlify config file",
        required=True
    )
    args = parser.parse_args()

    netlify_config = get_netlify_config(args.input_config_path)
    update_netlify_config_with_overrides(netlify_config, args.overrides_path)
    update_netlify_config_with_additions(netlify_config, args.additions_path)
    save_netlify_config(netlify_config, args.output_config_path)

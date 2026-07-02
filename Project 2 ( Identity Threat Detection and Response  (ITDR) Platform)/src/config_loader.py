import json
import os

def load_config():
    current_dir = os.path.dirname(__file__)
    project_root = os.path.dirname(current_dir)

    config_path = os.path.join(project_root, "config", "config.json")

    with open(config_path, "r") as file:
        config = json.load(file)

    return config
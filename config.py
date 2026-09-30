import yaml
from pathlib import Path

# Load configuration from a YAML file
CONFIG_FILE = Path('examples/example_configs.yaml')

try:
    with open(CONFIG_FILE) as file:
        config = yaml.safe_load(file)
except FileNotFoundError:
    raise FileNotFoundError(f'Configuration file not found at {CONFIG_FILE}')

def get_config(key):
    return config.get(key)

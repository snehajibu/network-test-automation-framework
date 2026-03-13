import yaml
import os

def load_config(path = "config.yaml"):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(base_dir,"config.yaml")
    with open(config_path,'r') as file:
        config = yaml.safe_load(file)
    return config
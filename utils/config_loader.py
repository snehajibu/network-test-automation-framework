# reads config.yaml file and return it as a Python dictionaryx`
import yaml #imports PyYAML library; used to convert YAML file -> dictionary
import os #provides file path utilies like dirname(), join()

def load_config(path = "config.yaml"):
    base_dir = os.path.dirname(os.path.dirname(__file__)) #__file__ -> current directory; this format will go one level up
    config_path = os.path.join(base_dir,"config.yaml")
    with open(config_path,'r') as file:
        config = yaml.safe_load(file)
    return config
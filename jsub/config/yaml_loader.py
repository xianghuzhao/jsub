import yaml

def file_ext():
    return ['yaml', 'yml']

def load(config_file):
    with open(config_file, 'r') as f:
        return yaml.load(f.read())

import yaml


def parse_config(path):
    with open(path) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data

import yaml
import os


def parse_config(path):
    filelist = os.listdir(path)
    data = []
    for file in filelist:
        with open(path + file) as f:
            data_config = yaml.load(f, Loader=yaml.FullLoader)
            data.append(data_config)
    return data

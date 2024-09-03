from configparser import ConfigParser


def get_config(category, item):
    config = ConfigParser()
    config.read('C:\\Users\\manju\\OneDrive\\Documents\\GitHub\\OrangeHRM_Test_Cases\\configuration\\config.ini')
    return config.get(category, item)

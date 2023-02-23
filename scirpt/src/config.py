import os
import configparser

class Config:
    __default = configparser.ConfigParser()
    __default.read(os.path.dirname(os.getcwd()) + '/config.ini')

    __init__ = lambda self: None

    @staticmethod
    def get(section, key):
        return Config.__default[section][key]
    
    @staticmethod
    def set(section, key, value):
        Config.__default[section][key] = value

# path = os.path.dirname(os.getcwd())
# config = configparser.ConfigParser()
# config.read(path + '/config.ini')

# print(path)
# print(config['API']['OPEN_AI_API_KEY'])

def initConfig():
    return Config()

def get(section, key):
    return Config.get(section, key)

def set(section, key, value):
    return Config.set(section, key, value)

__all__ = ['initConfig']
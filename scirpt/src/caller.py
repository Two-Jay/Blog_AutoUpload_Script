from abc import ABC, abstractmethod

class caller(ABC):
    @abstractmethod
    def call(self, config):
        pass

class openai_caller(caller):
    def __init__(self, config):
        self.__config = config

    def call(self):
        print(self.__config.get('OPENAI', 'API_KEY'))


def createCaller(api_type, config):
    if api_type == 'openai':
        return openai_caller(config)
    else:
        raise Exception('Unknown caller')

__all__ = ['createCaller']
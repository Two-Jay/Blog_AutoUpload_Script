from abc import ABC, abstractmethod

class caller(ABC):
    @abstractmethod
    def call(self, config):
        pass

def createCaller(config):
    api_type = config.get('API', 'API_TYPE')
    if api_type == 'openai':
        import open_api_caller
        return open_api_caller.openai_caller(config)
    else:
        raise Exception('Unknown caller')

def call(caller):
    caller.call()

__all__ = ['createCaller', 'call']
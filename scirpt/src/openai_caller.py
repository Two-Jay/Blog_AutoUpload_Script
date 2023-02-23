import caller

class openai_caller(caller.caller):
    def __init__(self, config):
        self.__config = config

    def call(self):
        print(self.__config.get('OPENAI_API_CONFIG', 'API_KEY'))
        print(self.__config.get('OPENAI_API_CONFIG', 'ENGINE'))
        print(self.__config.get('OPENAI_QUARY_CONFIG', 'TEMPERATURE'))


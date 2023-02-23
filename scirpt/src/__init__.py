import config as Config
import caller as Caller

def main():
    config = Config.initConfig()
    caller = Caller.createCaller(config.get("API", "API_TYPE"), config)
    caller.call()

if __name__ == '__main__':
    main()
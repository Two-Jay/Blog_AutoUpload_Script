import config as Config
import caller as Caller

def main():
    Caller.call(Caller.createCaller(Config.initConfig()))

if __name__ == '__main__':
    main()
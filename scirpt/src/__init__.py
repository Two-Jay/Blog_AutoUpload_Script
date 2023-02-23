import config

def main():
    print(config.get('API', 'OPEN_AI_API_KEY'))

if __name__ == '__main__':
    main()
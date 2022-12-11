import configparser

def making_config_ini():

    config = configparser.ConfigParser()
    config['SALE_JN'] = {
        'path' : r'C:\Users\Akabane NB 10\PycharmProjects\v3\sale_j.csv'
    }

    config['SALE_EN'] = {
        'path' : r'C:\Users\Akabane NB 10\PycharmProjects\v3\sale_e.csv'
    }

    config['IMPORT_CSV'] = {
        'path' : r'C:\Users\Akabane NB 10\PycharmProjects\v3\1.csv'
    }

    with open('config.ini', 'w') as config_file:
        config.write(config_file)

def reading_config_ini():

    config = configparser.ConfigParser()
    config.read('config.ini')

    sale_e = config['SALE_EN']['path']

if __name__ == '__main__':
    ...
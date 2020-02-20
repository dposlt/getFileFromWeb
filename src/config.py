import configparser


def getWebFromIni(inifile):
    config = configparser.ConfigParser()
    
    #config.read(inifile)

    if 'WEBSITE' in config:
        return config['WEBSITE']


print(getWebFromIni('config.ini'))
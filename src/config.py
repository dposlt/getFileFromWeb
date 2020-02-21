import configparser


def getWebFromIni(inifile):
    config = configparser.ConfigParser()
    
    #print(config.read(inifile))
    config.read(inifile)


    if 'DEFAULT' in config:
        web = config['DEFAULT']['Web']
        path = config['DEFAULT']['TargetPath']
        return web, path

#getWebFromIni('src\config.ini')

import urllib.request
import config

def openWeb(web):
    with urllib.request.urlopen(web) as f:
        print(f.read(300))


web,path = config.getWebFromIni('config.ini')

openWeb(web)
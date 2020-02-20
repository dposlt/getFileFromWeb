import urllib3

def openWeb(web):
    ow = urllib3.connection(web)
    return ow

openWeb
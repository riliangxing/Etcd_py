# /usr/bin/python
import ConfigParser
def _getConfig(sectioon, option):
    cf = ConfigParser.ConfigParser()
    f = open('config.ini')
    cf.readfp(f)
    p = cf.get(section=sectioon, option=option)
    f.close()
    return p






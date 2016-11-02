import os
from adn_getconfig import _getConfig

dir = _getConfig("path","localpath")
sspname = _getConfig("sspinfo","sspname")
sspnameArray = sspname.split('`')

def _checkSsp():
    bo = 1;
    if(len(sspnameArray) == 0):
        return 0
    if(sspnameArray[0].lower()=="all"):
        ssps = _getSsp(dir)
        for ssp in ssps:
            if(_CheckSignssp(ssp) != 1):
                bo =0;
                print "ssp "+ssp +" is error"
                break
    else:
        for sspN in sspnameArray:
            if(_CheckSignssp(sspN) != 1):
                bo =0;
                print sspN + " vm name is error"
                break
    return bo

def _CheckSignssp(sspN):
    bo = 1
    files = _getSspVm(sspN);
    if(len(files) != 5):
        print "the num of "+sspN+" vm is error "
        return 0
    for filename in files:
        if(filename.lower() != "mediatype"
            and filename.lower() != "method"
            and filename.lower() != "request.vm"
            and filename.lower() != "requrl.vm"
            and filename.lower() != "response.vm"):
            bo = 0 ;
            print "vm "+filename+ " is error"
            break
    return bo

def _getSspVm(sspN):
    dirssp = dir + "/" + sspN
    files = os.listdir(dirssp)
    return files

def _getSsp(dir):
    ssps = os.listdir(dir)
    return ssps

def _exitExcluelist(sspN):
    bo = 0;
    for exssp in sspnameArray:
        if(sspN == exssp):
            bo = 1
    return bo

from adn_checkSsp import _checkSsp
from adn_checkSsp import _getSspVm
from adn_checkSsp import dir
from adn_checkSsp import sspnameArray
from adn_checkSsp import _getSsp

def _getSspVms():
    SspVms = {}
    if(len(sspnameArray) > 0):
        if(sspnameArray[0] == "all"):
            ssps = _getSsp(dir)
            for ssp in ssps:
                SspVms[ssp] = _readVm(ssp)
        else:
            for sspname in sspnameArray:
                SspVms[sspname] = _readVm(sspname)
    return SspVms

def _readVm(ssp):
    signSspvm = {}
    sspvms = _getSspVm(ssp)
    for sspvm in sspvms:
        vmpath = dir + "/" + ssp + "/" + sspvm
        f = open(vmpath, "r")
        content = f.read()
        f.close()
        signSspvm[sspvm] = content
    return signSspvm

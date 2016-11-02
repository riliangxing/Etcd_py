import etcd
from adn_checkSsp import _checkSsp
from adn_getconfig import _getConfig
from adn_readSspvm import _getSspVms
from adn_writeSsp import _creatFile
from adn_writeSsp import _writeFile
from adn_writeSsp import _getfilename
from adn_checkSsp import sspnameArray

def _init_etcd(host, port):
    return etcd.Client(host=host, port=port)

def _putAdn(client,sspVmsMap):
    if client is None:
        print "etcd master connect is error"
        return
    etcdpath = _getConfig("path","etcdpath")
    for (kssp,vssp) in sspVmsMap.items():
        sspetcdpath = etcdpath + "/" + kssp
        for(kvm,vvm) in vssp.items():
            nodename = sspetcdpath + "/" + kvm
            client.write(nodename, vvm)

def _handlerCheckPut(client):
    option = _getConfig("option","option").strip()
    ssp = _getConfig("sspinfo","sspname").strip()
    if(int(option) == 0):
        print "just check wether "+ ssp + " vm file is correct"
        if(_checkSsp() == 1):
            print ssp + " vm file is complete"
    elif(int(option) == 1):
        sspVms = _getSspVms()
        print "check and put " + ssp + " vm to etcd"
        _putAdn(client,sspVms)
    elif(int(option) == 2):
        exportpath = _getConfig("path", "exportpath")
        for sspN in sspnameArray:
            _exportEtcd(client,sspN)
        print "export ssp vm to path : " + exportpath + " completely"

def _exportEtcd(client,sspN):
    etcdpath = _getConfig("path", "etcdpath")
    exportpath = _getConfig("path","exportpath")
    nodename = etcdpath + "/" + sspN
    exportssppath = exportpath + "/" + sspN
    _creatFile(exportssppath)
    result = client.read(nodename)
    for child in result.children:
        if child.key is not None:
            vmN = _getfilename(str(child.key))
            vmpath = exportssppath + "/" + vmN
            _writeFile(vmpath,str(child.value))

if __name__=="__main__":
    host = _getConfig("connection", "host").strip()
    port = int(_getConfig("connection", "port").strip())
    client = _init_etcd(host,port)
    _handlerCheckPut(client)
    print "Processing is completed "






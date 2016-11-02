import  os

def _creatFile(filepath):
    exist = os.path.exists(filepath)
    if exist == False:
        os.makedirs(filepath)
    return True

def _writeFile(filepath,vmValue):
    f = open(filepath, 'w')
    f.write(str(vmValue))
    f.close()
    return True

def _getfilename(filepath):
     files = str(filepath).split("/")
     size = int(len(files))
     return files[size-1]

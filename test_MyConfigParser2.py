from MyConfigParser2 import *
filePath = '/home/alex/PythonTasks/rawcontainer/RAW/Opt_Flat_st/ScanRawData.dat.ini'
filePath_1 = '/home/alex/PythonTasks/rawcontainer/RAW/Opt_Flat_st/ScanRawData_1.dat.ini'

D=readIniFile(filePath)
print D
writeIniFile(filePath_1, D)
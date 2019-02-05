from Strings import *
filePath = '/home/alex/PythonTasks/rawcontainer/RAW/Opt_Flat_st/ScanRawData.dat.ini'
filePath_1 = '/home/alex/PythonTasks/rawcontainer/RAW/Opt_Flat_st/ScanRawData_1.dat.ini'

Fin = open(filePath, 'r')
Fout = open(filePath_1, 'w')
lines = Fin.readlines()
D={}
params={}
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    if "[" in lines[i]:
        params = {}
        sname = string_before(lines[i],"]")
        sname = string_after(sname,"[")

        continue
    if "=" in lines[i]:
        key = string_before(lines[i],"=")
        value = string_after(lines[i], "=")
        params[key] = value

    D[sname] = params

Dout=D.copy()
keys=Dout.keys()
print keys
for k in keys:
    Fout.write("["+k+"]"+"\n")
    params=D.get(k)
    pkeys=params.keys()
    for k2 in pkeys:
        Fout.write(k2+"="+params.get(k2)+"\n")
    Fout.write("\n")

Fin.close()
Fout.close()

print D




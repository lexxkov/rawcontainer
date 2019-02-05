
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
        sname = lines[i][1:-1]

        continue
    if "=" in lines[i]:
        for j in range(len(lines[i])):
            if lines[i][j]=="=":
                key=lines[i][:j]
                value=lines[i][j+1:]
                params[key] = value
    D[sname] = params

Fin.close()
Fout.close()

print D




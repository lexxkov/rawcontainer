from Strings import *

def readIniFile(filePath):
    Fin = open(filePath, 'r')
    D={}
    D1={}
    for l in Fin:
        l = l.strip()
        if "[" in l:
            D1 = {}
            sname = string_before(l,"]")
            sname = string_after(sname,"[")

        if "=" in l:
            key = string_before(l,"=")
            value = string_after(l, "=")
            D1[key] = value

        D[sname] = D1
    Fin.close()
    return D

def writeIniFile(filePath, D):
    Fout = open(filePath, 'w')
    for k in D.keys():
        Fout.write("["+k+"]"+"\n")
        D1=D.get(k)
        for k1 in D1.keys():
            Fout.write(k1+"="+D1.get(k1)+"\n")
        Fout.write("\n")
    Fout.close()





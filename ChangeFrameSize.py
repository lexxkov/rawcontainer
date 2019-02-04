from RawContainer import *
import matplotlib.pyplot as plt


x1 = 50
x2 = 200
y1 = 0
y2 = 296
width2 = x2 - x1
height2 = y2 - y1


filePath = '/home/alex/PythonTasks/rawcontainer/RAW/Opt_Flat_st/ScanRawData'
Fin = RawContainerReader(filePath)
Fin.open()

simpleImage = Fin.readNextFrame() # single frame with number 0

im = plt.imshow(simpleImage, cmap='Greys')
plt.show(block=True)

Fin.close()

sliceRawData(filePath,filePath+'2',x1, y1, width2, height2)

Fin2 = RawContainerReader(filePath+'2')
Fin2.open()

simpleImage2 = Fin2.readNextFrame() # single frame with number 0

im = plt.imshow(simpleImage2, cmap='Greys')
plt.show(block=True)

Fin2.close()
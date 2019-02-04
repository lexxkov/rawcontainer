from RawContainer import *
import matplotlib.pyplot as plt

filePath = '/home/alex/PythonTasks/rawcontainer/RAW/Opt_Flat_st/ScanRawData'
Fin = RawContainerReader(filePath)
Fin.open()

width = Fin.width
height = Fin.height

Fout = RawContainerWriter(filePath+"1")
Fout.open(width, height)

while Fin.currentFrame < Fin.frameCount:
    simpleImage = Fin.readNextFrame() # single frame with number 0
    Fout.writeFrame(simpleImage)

im = plt.imshow(simpleImage, cmap='Greys')
plt.show(block=True)

Fin.close()
Fout.close()

Fin2 = RawContainerReader(filePath+'1')
Fin2.open()

while Fin2.currentFrame < Fin2.frameCount:
    simpleImage2 = Fin2.readNextFrame() # single frame with number 0

im = plt.imshow(simpleImage2, cmap='Greys')
plt.show(block=True)

Fin2.close()
from RawContainer import *
import matplotlib.pyplot as plt

filePath = '/home/alex/PythonTasks/rawcontainer/RAW/SMA/ScanRawData'
Fin = RawContainerReader(filePath)
Fin.open()

width = Fin.width
height = Fin.height

Fout = RawContainerWriter(filePath+"1")
Fout.open(width, height)
Fout.iniClone(Fin.iniConfig)
Fout.iniConfig.set('System', 'Width', width)
Fout.iniConfig.set('System', 'Height', height)
Fout.saveConfig()
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
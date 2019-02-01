import struct
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
# print simpleImage
# plt.ion()
# im = plt.imshow(simpleImage, cmap='Greys')
# plt.show(block=True)
# Fin.close()
    Fout.writeFrame(simpleImage)

Fout.close()

Fin2 = RawContainerReader(filePath+'1')
Fin2.open()
simpleImage2 = Fin2.readFrame(0) # single frame with number 0
print simpleImage2

# if simpleImage2 != None:
plt.ion()
im = plt.imshow(simpleImage2, cmap='Greys')
plt.show(block=True)

# def updatefig(*args):
#     if reader.currentFrame < reader.frameCount-1 :
#         arry = reader.readNextFrame()
#         im.set_array(arry)
#         print reader.currentFrame
#     return im,
#
# ani = animation.FuncAnimation(fig, updatefig, interval=70, blit=True)
# plt.show(block=True)




Fin2.close()
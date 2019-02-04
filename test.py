import struct
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

width = Fin.width
height = Fin.height

Fout = RawContainerWriter(filePath+"1", width2, height2)
Fout.open()

while Fin.currentFrame < Fin.frameCount:
    simpleImage = Fin.readNextFrame() # single frame with number 0
    # print simpleImage.size, simpleImage.dtype, simpleImage.itemsize
    # Fout.writeFrameBytes(simpleImage)
    Fout.writeFrame(simpleImage, x1, x2, y1, y2)

# print simpleImage.size
#plt.ion()
im = plt.imshow(simpleImage, cmap='Greys')
plt.show(block=True)

#plt.ion()
im = plt.imshow(simpleImage[y1:y2, x1:x2], cmap='Greys')
plt.show(block=True)
Fin.close()
Fout.close()

Fin2 = RawContainerReader(filePath+'1')
Fin2.open()
# simpleImage2 = Fin2.readFrame(0) # single frame with number 0
# print simpleImage2.size

while Fin2.currentFrame < Fin2.frameCount:
    simpleImage2 = Fin2.readNextFrame() # single frame with number 0
    # print simpleImage2.size, simpleImage2.dtype, simpleImage2.itemsize


# if simpleImage2 != None:
#plt.ion()
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
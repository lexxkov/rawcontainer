#!/usr/bin/env python
"""
An animated image
"""

from RawContainer import RawContainerReader
import matplotlib
print matplotlib.get_backend()
import matplotlib.rcsetup as rcsetup
print(rcsetup.all_backends)
matplotlib.use("TkAgg")  # this is for Ubuntu
import matplotlib.pyplot as plt
import matplotlib.animation as animation

filePath = '/home/alex/PythonTasks/rawcontainer/RAW/Opt_Flat_st/ScanRawData'
reader = RawContainerReader(filePath)
reader.open()
width = reader.width
height = reader.height

simpleImage = reader.readFrame(0) # single frame with number 0
print reader.currentFrame
plt.ion()  #Turns the interactive mode on.
fig = plt.figure()
im = plt.imshow(simpleImage, cmap='Greys')

def updatefig(*args):
    if reader.currentFrame < reader.frameCount-1 :
        arry = reader.readNextFrame()
        im.set_array(arry)
        print reader.currentFrame
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=70, blit=True)
plt.show(block=True)


reader.close()



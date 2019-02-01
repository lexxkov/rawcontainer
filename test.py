from __init__ import RawContainer
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
from RawContainer import RawContainerReader
F = RawContainerReader('/home/alex/PythonTasks/rawcontainer/RAW/Opt_Flat_st/ScanRawData')
F.open()
print F.readNextFrame()
print F.readNextFrame()
print F.frameCount
#print matplotlib.get_backend()
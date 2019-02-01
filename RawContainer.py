import sys
import os
import ConfigParser
import numpy as np


class RawContainerWriter:
    """Writes frame sequence in MaxInspect RawData format"""

    def __init__(self, baseFilename):
        pass

    @property
    def config(self):
        pass

    def open(self, width, height):
        self.datFn = self.baseFilename + ".dat"
        self.iniFn = self.baseFilename + ".dat.ini"
        self.datFile = open(self.datFn, "wb")

        self.iniConfig = ConfigParser.ConfigParser()
        self.iniConfig.optionxform = str
        self.iniConfig.add_section('Datasource')
        self.iniConfig.set('Datasource', 'Type', 'RawFrameSequence')
        self.iniConfig.add_section('System')
        self.iniConfig.set('System', 'Width', width)
        self.iniConfig.set('System', 'Height', height)
        self._saveConfig()

    def writeFrame(self, im):
        pass

    def writeFrameBytes(self, buff):
        pass

    def addParam(self, section, paramName, paramVal):
        if not section in self.iniConfig.sections():
            self.iniConfig.add_section(section)
        self.iniConfig.set(section, paramName, paramVal)
        self._saveConfig()

    def close(self):
        pass

    def _saveConfig(self):
        cfgfile = open(self.iniFn, 'w')
        self.iniConfig.write(cfgfile)
        cfgfile.close()

    def saveConfig(self):
        self._saveConfig()


class RawContainerReader:
#    """Read frame sequence in MaxInspect RawData format"""

    def __init__(self, baseFilename):
        self.baseFilename = baseFilename
        self.iniConfig = None

    @property
    def config(self):
        return self.iniConfig

    def open(self):
        self.datFn = self.baseFilename + ".dat"
        self.iniFn = self.baseFilename + ".dat.ini"
        self.datFile = open(self.datFn, "rb")

        self.iniConfig = ConfigParser.ConfigParser()
        self.iniConfig.optionxform = str
        self.iniConfig.read(self.iniFn)
        self.width = int(self.iniConfig.get('System', 'Width'))
        self.height = int(self.iniConfig.get('System', 'Height'))
        self.frameSize = self.width * self.height
        self.frameCount = os.path.getsize(self.datFn) / self.frameSize
        self.currentFrame = 0

    def close(self):
        self.datFile.close()

    def readNextFrame(self):
        pass

    def readFrame(self, frameNum):
        if frameNum >= self.frameCount:
            return None
        self.datFile.seek(frameNum * self.frameSize)
        bytes = self.datFile.read(self.frameSize)
        return np.frombuffer(bytes, "uint8", self.frameSize).reshape(self.height, self.width)

    def readNextFrame(self):
        self.currentFrame +=1
        if self.currentFrame >= self.frameCount:
            return None
        self.datFile.seek(self.currentFrame * self.frameSize)
        bytes = self.datFile.read(self.frameSize)
        return np.frombuffer(bytes, "uint8", self.frameSize).reshape(self.height, self.width)

class SurfaceReader:
    """Read Surface data in MaxInspect SurfaceDaa format"""

    def __init__(self, baseFilename):
        self.baseFilename = baseFilename
        self.iniConfig = None

    @property
    def config(self):
        return self.iniConfig

    def open(self):
        self.iniFn = self.baseFilename + ".ini"
        self.iniConfig = ConfigParser.ConfigParser()
        self.iniConfig.optionxform = str
        self.iniConfig.read(self.iniFn)
        self.width = int(self.iniConfig.get('System', 'Width'))
        self.height = int(self.iniConfig.get('System', 'Height'))
        self.frameSize = self.width * self.height

    def readHeightMap(self):
        self.datFnHeight = self.baseFilename + "_height.dat"
        self.datFile = open(self.datFnHeight, "rb")
        self.datFile.seek(0)
        bytes = self.datFile.read(self.frameSize * 8)
        self.datFile.close()
        return np.frombuffer(bytes, "float64", self.frameSize).reshape(self.height, self.width)

    def readSubtractedMap(self):
        self.datFnHeight = self.baseFilename + "_mask.dat"
        self.datFile = open(self.datFnHeight, "rb")
        self.datFile.seek(0)
        bytes = self.datFile.read(self.frameSize * 8)
        self.datFile.close()
        return np.frombuffer(bytes, "uint8", self.frameSize).reshape(self.height, self.width)

    def readModulationdMap(self):
        self.datFnHeight = self.baseFilename + "_modulation.dat"
        self.datFile = open(self.datFnHeight, "rb")
        self.datFile.seek(0)
        bytes = self.datFile.read(self.frameSize * 8)
        self.datFile.close()
        return np.frombuffer(bytes, "float64", self.frameSize).reshape(self.height, self.width)


def spliceRawData(inPath, outPath, shiftX, shiftY, width, height):
    pass
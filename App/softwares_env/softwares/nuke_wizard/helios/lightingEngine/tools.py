import nuke
import os



def getFilePath():

    path = nuke.getFilename("Aov's path", '*.exr', 'D:/')
    path = path.split('/')
    path.pop(-1)
    path = ('/').join(path) + '/'

    return path

def unselect_all():
    if nuke.selectedNodes():
        for i in nuke.selectedNodes():
            i['selected'].setValue(False)

def setReadRange(node, min, max):

    node['first'].setValue(int(min))
    node['last'].setValue(int(max))
    node['origfirst'].setValue(int(min))
    node['origlast'].setValue(int(max))

def setRange(min, max):

	nuke.root()['first_frame'].setValue(int(min))
	nuke.root()['last_frame'].setValue(int(max))

def getRange():
        
        AOV_PATH = os.environ['AOV_PATH']
        print AOV_PATH
        files = os.listdir(AOV_PATH)

        framesList = []

        for aov in files:
            if 'beauty'.upper() in aov.upper():
                framesList.append(aov)

        framesList.sort()
        minFrame = framesList[0].split('.')[-2]
        maxFrame = framesList[-1].split('.')[-2]
        if minFrame.isdigit():
            pass
        else:
            minFrame = 1
            maxFrame = 1

        return [int(minFrame), int(maxFrame)]

def setFormat():

	height = 50
	width = 50

	projectFormat = "{} {} current".format(height, width)

	nuke.addFormat(test)
	root = nuke.toNode('root')
	root['format'].setValue('current')
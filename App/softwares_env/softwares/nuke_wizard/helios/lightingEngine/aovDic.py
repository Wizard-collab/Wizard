import nuke
import os

def buildDic(reads_list):

    readsDic = dict()

    beautyRead = ''
    lightsReads = []
    shaderReads = []
    for read in reads_list:
        aov = read['file'].value()
        if 'BEAUTY_' in aov.upper() or 'BEAUTY.' in aov.upper():
            beautyRead = read
        if 'LGT' in aov.upper():
            lightsReads.append(read)
        if 'SHADER' in aov.upper():
            shaderReads.append(read)

    readsDic['BEAUTY'] = beautyRead
    readsDic['LGT'] = lightsReads
    readsDic['SHADER'] = shaderReads

    return readsDic
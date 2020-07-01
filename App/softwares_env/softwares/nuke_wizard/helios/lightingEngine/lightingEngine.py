import nukescripts
import os
import nuke

import tools as t
reload(t)
import aovDic as ad
reload(ad)
import build as b
reload(b)

class main():

    def __init__(self, reads_list = None):

        if not reads_list:
            self.reads_list = t.getFilePath()
        else:
            self.reads_list = reads_list

        
        readsDic = ad.buildDic(self.reads_list)
        
        lightingGroup = self.buildMainGraph(readsDic)
        
        self.buildLightingGroupGraph(lightingGroup, readsDic)
        

    def buildMainGraph(self, readsDic):

        # Create beauty read
        beautyRead = readsDic['BEAUTY']

        # Create lighting group
        t.unselect_all()
        lightingGroup = nuke.collapseToGroup()
        lightingGroup.setName('LIGHTING GROUP')

        # Connects nodes
        lightingGroup.setInput(0, beautyRead)
        lightingGroup.setSelected(True)
        nukescripts.connect_selected_to_viewer(0)

        return lightingGroup

    def buildLightingGroupGraph(self, lightingGroup, readsDic):

        mergeKnobList = []
        onKnobList = []
        soloKnobList = []
        accessReadList = []

        startDivider = nuke.Text_Knob('firstDivider', '')
        lightingGroup.addKnob(startDivider)

        # Create mainpath knob
        mainPathKnob = nuke.File_Knob('mainPathKnob', 'Main path')
        #mainPathKnob.setValue(self.aov_path)
        lightingGroup.addKnob(mainPathKnob)
        mainPathAccess = 'nuke.toNode("{}").knob("mainPathKnob").getValue()'.format(lightingGroup.name())

        updatePathKnobName = 'updatePath'
        updatePathKnob = nuke.PyScript_Knob(updatePathKnobName, 'UPDATE PATH')
        lightingGroup.addKnob(updatePathKnob)

        scriptsList = []

        # Begin working in the group

        lightingGroup.begin()
        # ___________________________________________

        inputNode = nuke.allNodes()[-1]
        inputNode.setSelected(True)
        outputNode = nuke.allNodes()[0]

        # Loop to import each aovs
        for aovRead in readsDic['LGT']:
            
            t.unselect_all()

            lightingGroup.end()

            t.unselect_all()

            aovRead.setSelected(True)
            nuke.nodeCopy('%clipboard%')
            aovRead.setSelected(False)
            nuke.delete(aovRead)

            lightingGroup.begin()

            nuke.nodePaste('%clipboard%')
            aovRead = nuke.selectedNode()

            aov = aovRead['file'].value()
            aovName = aov.split('/')[-1].split('lgt_')[-1].split('_main')[0].upper().split('.')[0]

            # Create read and connect it to the graph
            #aovRead = b.createRead(aov, aovName, True)

            # Store access to path
            getAovFileName = '\naovFileName = nuke.toNode("LIGHTING_GROUP.{}").knob("file").getValue({}).split("/")[-1]'.format(
                aovRead.name(), mainPathAccess)
            access = '\nnuke.toNode("LIGHTING_GROUP.{}").knob("file").setValue({}+aovFileName)'.format(aovRead.name(),
                                                                                                       mainPathAccess)
            accessReadList.append(getAovFileName + access)

            # Create expo tool and connect it to the aov read
            exposure1 = nuke.createNode("EXPTool")
            exposure1.setName(aovName + '_EXPOSURE')

            exposure1.setSelected(True)

            # Create Saturation Tool and connect it to the EXPTool

            saturation1 = nuke.createNode("Saturation")
            saturation1.setName(aovName + '_SATURATION')

            saturation1.setSelected(True)

            # Create Hue tool and connect it to the Saturation Tool

            HueCorrect1 = nuke.createNode("HueCorrect")
            HueCorrect1.setName(aovName + '_HUE')

            HueCorrect1.setSelected(False)

            merge1 = nuke.nodes.Merge(inputs=[inputNode, aovRead], operation='from', name=aovName + '_from')

            merge2 = nuke.nodes.Merge(inputs=[merge1, HueCorrect1], operation='plus', name=aovName + '_plus')

            inputNode = merge2

            # Create the group Knobs
            lightingGroup.end()

            # ____________________________________________________

            # Light section knob
            lightDivider = nuke.Text_Knob(aovName.upper() + '_lightSection', aovName)
            lightingGroup.addKnob(lightDivider)

            # ON/OFF knob
            onKnobName = aovName + '_lightOn'
            b.createBool(onKnobName, 'ON', 1, lightingGroup)

            # Solo knob
            soloKnobName = aovName + '_lightSolo'
            b.createBool(soloKnobName, 'SOLO', 0, lightingGroup)

            mixKnob = merge2.knob('mix')
            # mixKnob.setExpression(onKnobName)

            mergeKnobList.append(mixKnob)
            onKnobList.append(onKnobName)
            soloKnobList.append(soloKnobName)

            # AdjustIn knob
            adjustInKnob = exposure1.knob('mode')
            lightingGroup.addKnob(adjustInKnob)
            adjustInKnob.setValue('Stops')

            # Exposure knob
            expoFloat = nuke.Double_Knob(aovName + '_expoFloat', 'Exposure')
            lightingGroup.addKnob(expoFloat)
            nuke.toNode(lightingGroup.name()).knob(expoFloat.name()).setRange(-15, 15)
            redKnob = exposure1.knob('red')
            greenKnob = exposure1.knob('green')
            blueKnob = exposure1.knob('blue')

            redKnob.setExpression(expoFloat.name())
            greenKnob.setExpression(expoFloat.name())
            blueKnob.setExpression(expoFloat.name())

            # Reset knob
            resetKnobName = aovName + '_resetExpo'
            script = 'nuke.toNode("{}").knob("{}").setValue(0)'.format(lightingGroup.name(), aovName + '_expoFloat')
            scriptsList.append(script)
            resetKnob = nuke.PyScript_Knob('resetKnobName', 'RESET', script)
            lightingGroup.addKnob(resetKnob)

            # Saturation knob
            satFloat = nuke.Double_Knob(aovName + '_satFloat', 'Saturation')
            lightingGroup.addKnob(satFloat)
            nuke.toNode(lightingGroup.name()).knob(satFloat.name()).setRange(0, 15)
            saturationKnob = saturation1.knob('saturation')
            nuke.toNode(lightingGroup.name()).knob(satFloat.name()).setValue(1)
            saturationKnob.setExpression(satFloat.name())

            # Reset knob
            resetKnobName = aovName + '_resetSat'
            script = 'nuke.toNode("{}").knob("{}").setValue(1)'.format(lightingGroup.name(), aovName + '_satFloat')
            scriptsList.append(script)
            resetKnob = nuke.PyScript_Knob('resetKnobName', 'RESET', script)
            lightingGroup.addKnob(resetKnob)

            # ____________________________________________________

            lightingGroup.begin()

        for mK in mergeKnobList:

            value = mergeKnobList.index(mK)

            knobToRemove = soloKnobList[value]
            listWithoutMk = soloKnobList[:]
            listWithoutMk.pop(value)
            expressionList = []

            for i in listWithoutMk:
                expressionList.append('(1-{})'.format(i))

            soloExpression = (' * ').join(expressionList)

            mK.setExpression('{} * ({})'.format(onKnobList[value], soloExpression))

        outputNode.setInput(0, merge2)

        for n in nuke.allNodes():
            n.autoplace()

        # ___________________________________________

        lightingGroup.end()

        # ResetAll knob

        endDivider = nuke.Text_Knob('resetAllDider', '')
        lightingGroup.addKnob(endDivider)

        resetAllKnobName = 'resetAllExpo'
        # script = 'nuke.toNode("{}").knob("{}").setValue(0)'.format(lightingGroup.name(), aovName+'_expoFLoat')
        script = ('\n').join(scriptsList)
        resetAllKnob = nuke.PyScript_Knob('resetAllKnob', 'RESET ALL', script)
        lightingGroup.addKnob(resetAllKnob)

        # Connect all reads to main path
        getBeautyFileName = '\naovFileName = nuke.toNode("BEAUTY READ").knob("file").getValue().split("/")[-1]'
        access = '\nnuke.toNode("BEAUTY READ").knob("file").setValue({}+aovFileName)'.format(mainPathAccess)

        script = ('\n').join(accessReadList)


        updatePathKnob.setValue(script + getBeautyFileName + access)

        for n in nuke.allNodes():
            n.autoplace()
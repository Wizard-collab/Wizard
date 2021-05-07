import maya.cmds as cmds
import maya.mel as mel
from functools import partial
import datetime
import os


class easy_cloth():
    
    def __init__(self, *arg):
        
        self.nucleusList = cmds.ls(type='nucleus')
        self.clothWin = self.createUI()
        self.collideShader = 'colliderShader'


    def createUI(self, *arg):
        
        if cmds.window('easyClothWin', exists=1) == True:
            cmds.deleteUI('easyClothWin', window=1)
        
        clothWin = cmds.window('easyClothWin', title='easyCloth')
        mainForm = cmds.formLayout()
        bodyLayout = cmds.columnLayout(adj=1)
        
        nucleusFrame = cmds.frameLayout(l='Nucleus', parent=bodyLayout, collapsable=1, bgc=(0.18,0.18,0.18))
        cmds.text(l='', height=4)
        cmds.columnLayout(adj=0)
        cmds.rowColumnLayout(nc=3)
        self.nucleusMenu = cmds.optionMenu(l='Solver', changeCommand=self.changeNucleus)
        cmds.menuItem('New solver')
        for nucleus in self.nucleusList :
            cmds.menuItem(nucleus)
        if self.nucleusList != []:
            cmds.optionMenu(self.nucleusMenu, e=1, v=self.nucleusList[-1])
        cmds.text('   ')
        
        self.activeCheck = cmds.checkBox(l='Active', onc=partial(self.activateNucleus, 1), ofc=partial(self.activateNucleus, 0))
        cmds.setParent('..')
        
        if cmds.optionMenu(self.nucleusMenu, q=1, v=1) == 'New solver':
            self.nucleusNameField = cmds.textFieldGrp(l='Name', cl2=('left', 'right'), cw2=(44,94), columnAttach2=('left','right'), visible=1)
            self.nucleusFrameField = cmds.textFieldGrp(l='Start frame', cl2=('left', 'right'), cw2=(64,74), columnAttach2=('left','right'), visible=1, text='100')
            self.changeNucleus('New solver') 
        else:
            self.nucleusNameField = cmds.textFieldGrp(l='Name', cl2=('left', 'right'), cw2=(44,94), columnAttach2=('left','right'), visible=0)
            self.nucleusFrameField = cmds.textFieldGrp(l='Start frame', cl2=('left', 'right'), cw2=(64,74), columnAttach2=('left','right'), visible=0, text='100')
            self.changeNucleus(cmds.optionMenu(self.nucleusMenu, q=1, v=1))
        cmds.text(l='', height=4)
        cmds.button(l='Set Guff parameters', c=self.assignNucleusParam)
        
        cmds.text(l='', height=6)
        
        clothFrame = cmds.frameLayout(l='Cloth', collapsable=1, collapse=0, parent=bodyLayout, bgc=(0.18,0.18,0.18))
        cmds.columnLayout(adj=1, parent=clothFrame)
        cmds.text(l='', height=6)
        cmds.iconTextButton(l='Cloth', command=self.createCloth,i='nClothCreate.png',style='iconAndTextHorizontal', bgc=(0.35,0.35,0.35))
        cmds.text(l='', height=2)
        cmds.button(l='Set Guff parameters', command=self.guffCloth)

        cmds.text(l='', height=6)
        colliderFrame = cmds.frameLayout(l='Collider', collapsable=1, collapse=0, parent=bodyLayout, bgc=(0.18,0.18,0.18))
        cmds.columnLayout(adj=1, parent=colliderFrame)
        cmds.text(l='', height=6)
        self.smoothMenu = cmds.optionMenu(l='Smooth division')
        cmds.menuItem(l='0')
        cmds.menuItem(l='1')
        cmds.menuItem(l='2')
        cmds.menuItem(l='3')
        cmds.menuItem(l='4')
        cmds.optionMenu(self.smoothMenu, e=1, v='2')
        cmds.text(l='', height=2)
        cmds.iconTextButton(l='Collider', command=self.createCollider,i='nClothCreatePassive.png',style='iconAndTextHorizontal', bgc=(0.35,0.35,0.35))
        cmds.text(l='', height=2)

        cmds.button(l='Set Guff parameters', command=self.guffCollider)
        cmds.text(l='', height=6)
        
        constraintFrame = cmds.frameLayout(l='Constraints', collapsable=1, collapse=1, parent=bodyLayout, bgc=(0.18,0.18,0.18))
        cmds.columnLayout(adj=1, parent=constraintFrame)
        cmds.text(l='', height=6)
        cmds.button(l='Transform', align='left', command=self.cTransform)
        cmds.text(l='', height=2)
        cmds.button(l='Point to surface', command=self.cPoint)
        cmds.text(l='', height=2)
        cmds.button(l='Slide on surface', command=self.cSlide)
        cmds.text(l='', height=2)
        cmds.button(l='Component to component', command=self.cComponent)
        cmds.text(l='', height=6)

        nCacheColumn = cmds.columnLayout(parent=mainForm, adj=1)
        nCacheButton = cmds.iconTextButton(l='nCache ( in scene directory )   ', command=self.nCache,i='nClothCacheCreate.png',style='iconAndTextHorizontal', bgc=(0.35,0.35,0.35),width = 200)
        cmds.text(l='', height=2)
        nCacheButton = cmds.iconTextButton(l='nCache ( in scene directory ) HD', command=self.nCacheHD,i='nClothCacheCreate.png',style='iconAndTextHorizontal', bgc=(0.35,0.35,0.35),width = 200)
        cmds.text(l='', height=6)
        
        
        
        cmds.formLayout(mainForm, e=1, attachForm=[(nCacheColumn,'bottom',10),(nCacheColumn,'left',10),(nCacheColumn,'right',10),(bodyLayout,'top',10),(bodyLayout,'bottom',10),(bodyLayout,'left',10),(bodyLayout,'right',10)])
        return(clothWin)
        
    def showUI(self, *arg):
        cmds.showWindow(self.clothWin)

    def cTransform(self, *arg):
        mel.eval('createNConstraint transform 0;')

    def cPoint(self, *arg):
        mel.eval('createNConstraint pointToSurface 0;')

    def cSlide(self, *arg):
        mel.eval('createNConstraint slideOnSurface 0;')

    def cComponent(self, *arg):
        mel.eval('createNConstraint pointToPoint 0;')


    def changeNucleus(self, item):
        if item == 'New solver':
            cmds.textFieldGrp(self.nucleusNameField, e=1, visible=1)
            cmds.textFieldGrp(self.nucleusFrameField, e=1, visible=1)
            cmds.checkBox(self.activeCheck, e=1, value=1, enable=0)
        else:
            cmds.textFieldGrp(self.nucleusNameField, e=1, visible=0, text='')
            cmds.textFieldGrp(self.nucleusFrameField, e=1, visible=0)
            nucleusState = cmds.getAttr(item+'.enable')
            if nucleusState:
                cmds.checkBox(self.activeCheck, e=1, value=1, enable=1)
            else:
                cmds.checkBox(self.activeCheck, e=1, value=0, enable=1)

        
    def activateNucleus(self, activate, *arg):
        nucleus = cmds.optionMenu(self.nucleusMenu, q=1, v=1)
        cmds.setAttr(nucleus+'.enable',activate)
        

    def assignNucleusParam(self, nucleus='', *arg):
        
        if nucleus == False or nucleus:
            nucleus = cmds.optionMenu(self.nucleusMenu, q=1, v=1)

        cmds.setAttr(nucleus+'.subSteps', 12)
        cmds.setAttr(nucleus+'.maxCollisionIterations', 24)
        cmds.setAttr(nucleus+'.spaceScale', 0.1)


    def startFrame(self, nucleus, *arg):
        if nucleus == False or nucleus:
            nucleus = cmds.optionMenu(self.nucleusMenu, q=1, v=1)

        startFrame = int(cmds.textFieldGrp(self.nucleusFrameField, q=1, text=1))

        cmds.setAttr(nucleus+'.startFrame', startFrame)

    def createCloth (self, *arg):
 
        objList = cmds.ls(sl=1)
        if objList == []:
            cmds.warning('Please select an object')
              
        if cmds.objExists('sim_GRP') == 0:
            cmds.group(em=1, name='sim_GRP')
                        
        for obj in objList :
            if ':' in obj:newObj=obj.split(':')[-1]
            else: newObj=obj
            choosenNucleus = cmds.optionMenu(self.nucleusMenu, q=1, v=1) 

            objSimGrp = cmds.group(empty = 1, name = '{}_sim_GRP'.format(obj), parent = 'sim_GRP')
            simObj = cmds.duplicate(obj, name = '{}_sim'.format(obj))
            cmds.parent(simObj, objSimGrp)
            cmds.setAttr(obj+'.visibility', 0)      
            blendShapeName = '{}_blendShape'.format(obj)
            cmds.blendShape(obj, simObj, origin='world', name=blendShapeName )
            cmds.setAttr(blendShapeName+'.'+ newObj, 1)
            nClothShape = mel.eval('createNCloth 0;')
            nClothNode = cmds.listRelatives(nClothShape, parent=1)
            nClothNode = cmds.rename(nClothNode, '{}_nCloth'.format(obj))
            cmds.parent(nClothNode, objSimGrp)
            cmds.select(simObj, replace=1)
            self.guffCloth()
            cmds.select(nClothNode, replace=1)
            if choosenNucleus == 'New solver' and self.nucleusList != []:
                nucleusName = cmds.textFieldGrp(self.nucleusNameField, q=1, text=1)
                nucleusNode = cmds.createNode('nucleus', n=nucleusName)
                cmds.select(nClothNode)
                cmds.connectAttr('time1.outTime', nucleusNode + '.currentTime') 
                mel.eval('assignNSolver {};'.format(nucleusNode))
                self.addNucleusNode(nucleusNode)
                self.assignNucleusParam(nucleusNode)
                self.startFrame(nucleusNode)
            elif choosenNucleus == 'New solver' and self.nucleusList == []:
                nucleusName = cmds.textFieldGrp(self.nucleusNameField, q=1, text=1)
                if nucleusName != '':
                    nucleusNode = cmds.createNode('nucleus', n=nucleusName)
                    cmds.select(nClothNode)
                    cmds.connectAttr('time1.outTime', nucleusNode + '.currentTime') 
                    mel.eval('assignNSolver {};'.format(nucleusNode))
                    cmds.delete('nucleus1')
                    self.addNucleusNode(nucleusNode)
                    self.assignNucleusParam(nucleusNode)
                    self.startFrame(nucleusNode)
                else:
                    self.addNucleusNode('nucleus1')
                    self.assignNucleusParam('nucleus1')
                    self.startFrame('nucleus1')
            else:
                mel.eval('assignNSolver {};'.format(choosenNucleus))
    
    def guffCollider(self,*arg):
        objList = cmds.ls(sl=1)
        if objList == []:
            cmds.warning('Please select an object')
        for obj in objList:
            objShape = cmds.listRelatives(obj, shapes=1)[0]
            colliderObj = cmds.listConnections(objShape, type='nRigid')[0]
            colliderShape = cmds.listRelatives(colliderObj, shapes=1)[0]
            cmds.setAttr(colliderShape+'.isDynamic',1)
            cmds.setAttr(colliderShape+'.depthSort',0)
            try:cmds.setAttr(colliderShape+'.playFromCache',0)
            except:pass
            cmds.setAttr(colliderShape+'.thickness',0.102)
            cmds.setAttr(colliderShape+'.bounce',0)
            cmds.setAttr(colliderShape+'.friction',0.1)
            cmds.setAttr(colliderShape+'.damp',0)
            cmds.setAttr(colliderShape+'.stickiness',0)
            cmds.setAttr(colliderShape+'.collideStrength',1)
            cmds.setAttr(colliderShape+'.collisionFlag',3)
            cmds.setAttr(colliderShape+'.selfCollisionFlag',1)
            cmds.setAttr(colliderShape+'.maxSelfCollisionIterations',4)
            cmds.setAttr(colliderShape+'.maxIterations',10000)
            cmds.setAttr(colliderShape+'.pointMass',1)
            cmds.setAttr(colliderShape+'.restLengthScale',1)
            cmds.setAttr(colliderShape+'.localForceX',0)
            cmds.setAttr(colliderShape+'.localForceY',0)
            cmds.setAttr(colliderShape+'.localForceZ',0)
            cmds.setAttr(colliderShape+'.localWindX',0)
            cmds.setAttr(colliderShape+'.localWindY',0)
            cmds.setAttr(colliderShape+'.localWindZ',0)
            cmds.setAttr(colliderShape+'.collide',1)
            cmds.setAttr(colliderShape+'.selfCollide',0)
            cmds.setAttr(colliderShape+'.collisionLayer',0)
            cmds.setAttr(colliderShape+'.windShadowDiffusion',0)
            cmds.setAttr(colliderShape+'.windShadowDistance',0)
            cmds.setAttr(colliderShape+'.airPushDistance',0)
            cmds.setAttr(colliderShape+'.airPushVorticity',0)
            cmds.setAttr(colliderShape+'.pushOut',0)
            cmds.setAttr(colliderShape+'.pushOutRadius',0)
            cmds.setAttr(colliderShape+'.crossoverPush',0)
            cmds.setAttr(colliderShape+'.trappedCheck',1)
            cmds.setAttr(colliderShape+'.forceField',0)
            cmds.setAttr(colliderShape+'.fieldMagnitude',1)
            cmds.setAttr(colliderShape+'.fieldDistance',1)
            cmds.setAttr(colliderShape+'.pointForceField',0)
            cmds.setAttr(colliderShape+'.pointFieldMagnitude',1)
            cmds.setAttr(colliderShape+'.selfAttract',0)
            cmds.setAttr(colliderShape+'.pointFieldDistance',2)
            cmds.setAttr(colliderShape+'.localSpaceOutput',0)
            cmds.setAttr(colliderShape+'.displayColorR',1)
            cmds.setAttr(colliderShape+'.displayColorG',0.8)
            cmds.setAttr(colliderShape+'.displayColorB',0)

    def guffCloth(self,*arg):
        objList = cmds.ls(sl=1)
        if objList == []:
            cmds.warning('Please select an object')
        for obj in objList:
            objShape = cmds.listRelatives(obj, shapes=1)
            clothObj = cmds.listConnections(objShape, type='nCloth', source=1, destination=0)[0]
            clothShape = cmds.listRelatives(clothObj, shapes=1)[0]
            cmds.setAttr(clothShape+'.isDynamic',1)
            cmds.setAttr(clothShape+'.depthSort',0)
            try:cmds.setAttr(clothShape+'.playFromCache',0)
            except:pass
            cmds.setAttr(clothShape+'.thickness',0.058)
            cmds.setAttr(clothShape+'.bounce',0)
            cmds.setAttr(clothShape+'.friction',0.1)
            cmds.setAttr(clothShape+'.damp',0.01)
            cmds.setAttr(clothShape+'.stickiness',0)
            cmds.setAttr(clothShape+'.collideStrength',1)
            cmds.setAttr(clothShape+'.collisionFlag',3)
            cmds.setAttr(clothShape+'.selfCollisionFlag',1)
            cmds.setAttr(clothShape+'.maxSelfCollisionIterations',64)
            cmds.setAttr(clothShape+'.maxIterations',10000)
            cmds.setAttr(clothShape+'.pointMass',1)
            cmds.setAttr(clothShape+'.restLengthScale',1)
            cmds.setAttr(clothShape+'.localForceX',0)
            cmds.setAttr(clothShape+'.localForceY',0)
            cmds.setAttr(clothShape+'.localForceZ',0)
            cmds.setAttr(clothShape+'.localWindX',0)
            cmds.setAttr(clothShape+'.localWindY',0)
            cmds.setAttr(clothShape+'.localWindZ',0)
            cmds.setAttr(clothShape+'.collide',1)
            cmds.setAttr(clothShape+'.selfCollide',1)
            cmds.setAttr(clothShape+'.collisionLayer',0)
            cmds.setAttr(clothShape+'.windShadowDiffusion',0)
            cmds.setAttr(clothShape+'.windShadowDistance',0)
            cmds.setAttr(clothShape+'.airPushDistance',0)
            cmds.setAttr(clothShape+'.airPushVorticity',0)
            cmds.setAttr(clothShape+'.pushOut',0)
            cmds.setAttr(clothShape+'.pushOutRadius',0.231)
            cmds.setAttr(clothShape+'.crossoverPush',0)
            cmds.setAttr(clothShape+'.trappedCheck',0)
            cmds.setAttr(clothShape+'.forceField',0)
            cmds.setAttr(clothShape+'.fieldMagnitude',1)
            cmds.setAttr(clothShape+'.fieldDistance',1)
            cmds.setAttr(clothShape+'.pointForceField',0)
            cmds.setAttr(clothShape+'.pointFieldMagnitude',1)
            cmds.setAttr(clothShape+'.selfAttract',0)
            cmds.setAttr(clothShape+'.pointFieldDistance',2)
            cmds.setAttr(clothShape+'.localSpaceOutput',1)
            cmds.setAttr(clothShape+'.displayColorR',1)
            cmds.setAttr(clothShape+'.displayColorG',0.8)
            cmds.setAttr(clothShape+'.displayColorB',0)
            cmds.setAttr(clothShape+'.stretchResistance',200)
            cmds.setAttr(clothShape+'.compressionResistance',30)
            cmds.setAttr(clothShape+'.bendResistance',1)
            cmds.setAttr(clothShape+'.bendAngleDropoff',0.3)
            cmds.setAttr(clothShape+'.restitutionTension',1000)
            cmds.setAttr(clothShape+'.restitutionAngle',360)
            cmds.setAttr(clothShape+'.shearResistance',0)
            cmds.setAttr(clothShape+'.rigidity',0)
            cmds.setAttr(clothShape+'.usePolygonShells',0)
            cmds.setAttr(clothShape+'.deformResistance',0)
            cmds.setAttr(clothShape+'.inputMeshAttract',0)
            cmds.setAttr(clothShape+'.collideLastThreshold',0.2)
            cmds.setAttr(clothShape+'.inputAttractDamp',0.5)
            cmds.setAttr(clothShape+'.inputMotionDrag',0)
            cmds.setAttr(clothShape+'.wrinkleMapScale',1)
            cmds.setAttr(clothShape+'.bendAngleScale',1)
            cmds.setAttr(clothShape+'.sortLinks',0)
            cmds.setAttr(clothShape+'.addCrossLinks',1)
            cmds.setAttr(clothShape+'.stretchDamp',200)
            cmds.setAttr(clothShape+'.selfCollideWidthScale',3)
            cmds.setAttr(clothShape+'.selfCrossoverPush',0)
            cmds.setAttr(clothShape+'.selfTrappedCheck',0)
            cmds.setAttr(clothShape+'.pressure',0)
            cmds.setAttr(clothShape+'.startPressure',0)
            cmds.setAttr(clothShape+'.incompressibility',5)
            cmds.setAttr(clothShape+'.pressureDamping',0)
            cmds.setAttr(clothShape+'.pumpRate',0)
            cmds.setAttr(clothShape+'.airTightness',1)
            cmds.setAttr(clothShape+'.sealHoles',1)
            cmds.setAttr(clothShape+'.ignoreSolverGravity',0)
            cmds.setAttr(clothShape+'.ignoreSolverWind',0)
            cmds.setAttr(clothShape+'.windSelfShadow',0)
            cmds.setAttr(clothShape+'.lift',0.02)
            cmds.setAttr(clothShape+'.drag',0.01)
            cmds.setAttr(clothShape+'.tangentialDrag',0.2)


    def createCollider (self, *arg):
        
        
        
        objList = cmds.ls(sl=1)
        if objList == []:
            cmds.warning('Please select an object')
        
        self.createShader()

        if cmds.objExists('sim_GRP') == 0:
            cmds.group(em=1, name='sim_GRP')

        smoothDiv = cmds.optionMenu(self.smoothMenu, q=1, v=1)
        
        for obj in objList :
            if ':' in obj:newObj=obj.split(':')[-1]
            else: newObj=obj
            choosenNucleus = cmds.optionMenu(self.nucleusMenu, q=1, v=1) 
            
            objColGrp = cmds.group(empty = 1, name = '{}_collider_GRP'.format(obj), parent = 'sim_GRP')
            colObj = cmds.duplicate(obj, name = '{}_collider'.format(obj))
            self.assignShader(colObj)
            cmds.parent(colObj, objColGrp)
            cmds.setAttr(obj+'.visibility', 0)      
            blendShapeName = '{}_blendShape'.format(obj)
            cmds.blendShape(obj, colObj, origin='world', name=blendShapeName )
            cmds.setAttr(blendShapeName+'.'+ newObj, 1)
            cmds.polySmooth(colObj, dv=int(smoothDiv))
            nRigidShape = mel.eval('makeCollideNCloth;')
            nRigidNode = cmds.listRelatives(nRigidShape, parent=1)
            nRigidNode = cmds.rename(nRigidNode, '{}_nRigid'.format(obj))
            cmds.parent(nRigidNode, objColGrp)
            cmds.select(colObj, replace=1)
            
            self.guffCollider()
            cmds.select(nRigidNode, replace=1)
            if choosenNucleus == 'New solver' and self.nucleusList != []:
                nucleusName = cmds.textFieldGrp(self.nucleusNameField, q=1, text=1)
                nucleusNode = cmds.createNode('nucleus', n=nucleusName)
                cmds.select(nRigidNode)
                cmds.connectAttr('time1.outTime', nucleusNode + '.currentTime') 
                mel.eval('assignNSolver {};'.format(nucleusNode))
                self.addNucleusNode(nucleusNode)
                self.assignNucleusParam(nucleusNode)
                self.startFrame(nucleusNode)
            elif choosenNucleus == 'New solver' and self.nucleusList == []:
                nucleusName = cmds.textFieldGrp(self.nucleusNameField, q=1, text=1)
                if nucleusName != '':
                    nucleusNode = cmds.createNode('nucleus', n=nucleusName)
                    cmds.select(nRigidNode)
                    cmds.connectAttr('time1.outTime', nucleusNode + '.currentTime') 
                    mel.eval('assignNSolver {};'.format(nucleusNode))
                    cmds.delete('nucleus1')
                    self.addNucleusNode(nucleusNode)
                    self.assignNucleusParam(nucleusNode)
                    self.startFrame(nucleusNode)
                else:
                    self.addNucleusNode('nucleus1')
                    self.assignNucleusParam('nucleus1')
                    self.startFrame('nucleus1')
            else:
                mel.eval('assignNSolver {};'.format(choosenNucleus))
    
    def addNucleusNode(self, nucleusNode):
        cmds.menuItem(l=nucleusNode, parent=self.nucleusMenu)
        self.nucleusList.append(nucleusNode)
        cmds.optionMenu(self.nucleusMenu, e=1, v=nucleusNode)
        self.changeNucleus(nucleusNode)


    def assignShader(self, obj, *arg):
        cmds.select(obj[0])
        cmds.hyperShade(assign=self.collideShader)


    def createShader(self, *arg):
        if not cmds.objExists('colliderShader'):
            self.collideShader = cmds.shadingNode('lambert', shared=True, asShader=True, name = 'colliderShader')
            cmds.setAttr(self.collideShader+'.colorR', 0.7)
            cmds.setAttr(self.collideShader+'.colorG', 0.2)
            cmds.setAttr(self.collideShader+'.colorB', 0.2)


    def nCache(self, HD=False, *args):

        objList = cmds.ls(sl=1)
        if objList == []:
            cmds.warning('Please select an object')

        for obj in objList:
            
            if ':' in obj:
                objName = obj.replace(':','_')
            else: objName = obj

            objShape = cmds.listRelatives(obj, shapes=1)
            clothObj = cmds.listConnections(objShape, type='nCloth', source=1)[0]
            clothShape = cmds.listRelatives(clothObj, shapes=1)

            ncloth_path = os.path.join(os.path.dirname(cmds.file(q=True, sn=True)), 'ncloth')
            if not os.path.isdir(ncloth_path):
                os.makedirs(ncloth_path)
            cachePath = increment_folder(os.path.join(ncloth_path,'cache')).replace('\\', '/')
            if HD==True:
                melCommand = 'doCreateNclothCache 5 { "2", "1", "10", "OneFile", "1", "' + cachePath + '","0","' + obj + '","0", "replace", "0", "0.2", "1","0","1","mcx" } ;'
            else:
                melCommand = 'doCreateNclothCache 5 { "2", "1", "10", "OneFile", "1", "' + cachePath + '","0","' + obj + '","0", "replace", "0", "1", "1","0","1","mcx" } ;'
            mel.eval(melCommand)


    def nCacheHD(self,*arg):
        self.nCache(HD=True)

def increment_folder(folder_name):

    num=1

    folder = "{}_{}".format(folder_name, str(num).zfill(4))

    while os.path.isdir(folder):
        num+=1
        folder = "{}_{}".format(folder_name, str(num).zfill(4))

    os.makedirs(folder)

    return folder
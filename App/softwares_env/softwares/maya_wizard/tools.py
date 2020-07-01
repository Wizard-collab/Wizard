import maya.cmds as cmds

def clean():

    objList = cmds.ls(sl=1)

    if objList == []:
        cmds.warning('Please select an object')

    try:cmds.loadPlugin( 'objExport.mll' )
    except:pass

    tempPath = cmds.internalVar(userTmpDir=True)

    for obj in objList:
        parentNode = cmds.listRelatives(obj, parent=1)
        cmds.select(obj, replace=1)
        tempFile=tempPath+obj+'.obj'
        cmds.file(tempFile, force=1, options='groups=0;ptgroups=0;materials=0;smoothing=0;normals=0', type='OBJexport', es=1)
        newNode = cmds.file(tempFile, i=1, returnNewNodes=1)[0]
        cmds.delete(obj)
        cmds.rename(newNode, obj)
        try:cmds.parent(obj, parentNode)
        except:pass
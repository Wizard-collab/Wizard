import pymel.core as pm

if pm.window('guerillaTagsWindow', q=1, exists=1):
    pm.deleteUI('guerillaTagsWindow')


def tagGuerilla(*arg):
    mesh_List = pm.ls(sl=1)
    slectionChild_List = pm.listRelatives(mesh_List, ad=1)
    if mesh_List:
        tagName = tagGuerillaText.getText()
        for mesh in slectionChild_List:
            parentMesh = mesh.getParent()
            if mesh.nodeType() == 'mesh' or mesh.nodeType() == 'camera':
                if pm.iconTextButton(addMoreTagButton, q=1, l=1) == 'off':
                    if pm.attributeQuery('GuerillaTags', node=parentMesh, exists=1) == 1:
                        pm.setAttr(parentMesh.GuerillaTags, tagName, type="string")

                    elif pm.attributeQuery('GuerillaTags', node=parentMesh, exists=1) == 0:
                        pm.addAttr(parentMesh, ln="GuerillaTags", dt="string")

                        pm.setAttr(parentMesh.GuerillaTags, tagName, type="string")

                elif pm.iconTextButton(addMoreTagButton, q=1, l=1) == 'on':
                    if pm.attributeQuery('GuerillaTags', node=parentMesh, exists=1):
                        currentAttr = parentMesh.name() + '.GuerillaTags'
                        currentTag = pm.getAttr(currentAttr)
                        currentSplit = currentTag.split(',')
                        checker_if_tag_in = 'no'
                        for tag in currentSplit:
                            if tag == tagName:
                                checker_if_tag_in = 'yes'

                        if checker_if_tag_in == 'no':
                            totalName = currentTag + ',' + tagName
                            pm.setAttr(parentMesh.GuerillaTags, totalName, type="string")

                    elif pm.attributeQuery('GuerillaTags', node=parentMesh, exists=1) == 0:

                        pm.addAttr(parentMesh, ln="GuerillaTags", dt="string")

                        pm.setAttr(parentMesh.GuerillaTags, tagName, type="string")


    else:
        pm.warning('Select object to assign Guerilla Tags')


def tagGuerillaAuto(*arg):
    selectionGuerilla_List = pm.ls(sl=1)
    if selectionGuerilla_List:
        for mesh in selectionGuerilla_List:
            if pm.attributeQuery('GuerillaTags', node=mesh, exists=1) == 0:
                pm.addAttr(mesh, ln="GuerillaTags", dt="string")

            pm.setAttr(mesh + '.GuerillaTags', mesh.name(), type="string")
    else:
        pm.warning('Your selection is empty')


def switchGuerillatagOption(*arg):
    if pm.iconTextButton(addMoreTagButton, q=1, l=1) == 'off':
        pm.iconTextButton(addMoreTagButton, e=1, l='on', image1='addClip.png')
        pm.textField(tagGuerillaText, e=1, bgc=(0.16862745098039217, 0.16862745098039217, 0.16862745098039217),
                     placeholderText='add one more tag')


    else:
        pm.iconTextButton(addMoreTagButton, e=1, l='off', image1='UVTkDeleteInvalidSet.png')
        pm.textField(tagGuerillaText, e=1, bgc=(0.3, 0.2, 0.2), placeholderText='replace Tags')


pm.window('guerillaTagsWindow', t='Guerilla Tags', sizeable=False, mxb=0, mnb=0)
pm.frameLayout(l='Guerilla Tags Tool', mw=5, mh=5)
pm.columnLayout(adj=True)
pm.separator(style='none', h=5)

pm.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 20), (2, 200), (3, 19)])
pm.iconTextButton(style='iconAndTextVertical', height=19, width=19, noBackground=True, image1='mGuerilla.png',
                  command=tagGuerillaAuto, annotation='AutoTags your selection for guerilla')

tagGuerillaText = pm.textField(aie=1, ec=tagGuerilla, placeholderText='add one more tag',
                               bgc=(0.16862745098039217, 0.16862745098039217, 0.16862745098039217))
addMoreTagButton = pm.iconTextButton(l='on', style='iconOnly', image1='addClip.png', height=19, width=19, ebg=False,
                                     command=switchGuerillatagOption,
                                     annotation='Switch between Add mode and Replace mode')

pm.setParent('..')

pm.separator(style='none', h=5)

pm.button(l='Set Guerilla Tags', c=tagGuerilla)

pm.showWindow()

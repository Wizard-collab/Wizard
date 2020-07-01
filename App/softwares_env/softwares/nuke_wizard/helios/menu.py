import nuke
import os

menubar = nuke.menu("Nuke")
thanosMenu = menubar.addMenu('Helios')
thanosMenu.addCommand( 'Light Engine', "import nuke_wizard.helios.lightingEngine.lightingEngine as lg\nreload(lg)\nlg.main()" )
thanosMenu.addCommand( 'Set OCIO', "import nuke_wizard.helios.scripts.setOCIO as setOCIO" )



iconFolder = os.path.abspath('./softwares_env/softwares/nuke_wizard/helios/Ressources/icons').replace('\\', '/')
FoldersDir = os.path.abspath('./softwares_env/softwares/nuke_wizard/helios/Ressources/gizmo').replace('\\', '/')
EffectsFoldersList = os.listdir(FoldersDir)

script = ("nuke.createNode(pathToNode)")

for folderEffect in EffectsFoldersList :
    gizmosset = menubar.addMenu('Helios/Effects/{}'.format(folderEffect), icon="effect.png")

    GizmosList = os.listdir('./softwares_env/softwares/nuke_wizard/helios/Ressources/gizmo/{}'.replace('\\', '/').format(folderEffect))
    for gizmo in GizmosList:
        gizmoName = gizmo.replace('.gizmo', "")
        command = script.replace('pathToNode','"{}"'.format(FoldersDir+'/'+folderEffect+'/'+gizmo)).replace('nodeName', '"{}"'.format(gizmoName))
        gizmosset.addCommand(gizmoName, command)

thanosMenu.addSeparator()
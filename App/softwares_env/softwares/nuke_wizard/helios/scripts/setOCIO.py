import nuke
import nukescripts.ViewerProcess;nukescripts.ViewerProcess.unregister_viewers("P:/NUKE/Nuke11.0v3/plugins/OCIOConfigs/configs/nuke-default/config.ocio");
import nukescripts.ViewerProcess; nukescripts.ViewerProcess._register_viewer_processes(defaultLUTS = False, ocioConfigName = "P:/NUKE/Nuke11.0v3/plugins/OCIOConfigs/configs/nuke-default/config.ocio");
nuke.tcl('knob root.colorManagement ' '1')
nuke.tcl('knob root.OCIO_config ' '3')
curViewer = nuke.activeViewer()
viewerNode = curViewer.node()
viewerNode['viewerProcess'].setValue( '10' )
import QtQuick 2.2
import Painter 1.0

PainterPlugin {
    
    /* called after the object has been instantiated. Used to execute script code at startup,
    once the full QML environment has been established. */
    Component.onCompleted:{
        //create a toolbar button
        alg.ui.addToolBarWidget("save.qml");
    }
}
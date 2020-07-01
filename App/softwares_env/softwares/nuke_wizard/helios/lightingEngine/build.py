import nuke
import tools as t
reload(t)
import os

#

def createRead(FILE, NAME, SELECT = False, RANGE = None):

	read = nuke.nodes.Read(file=FILE, name=NAME)

	read.setSelected(SELECT)

	return read

def createBool(NAME, LABEL, VALUE, HOST):
	
	onKnob = nuke.Boolean_Knob(NAME, LABEL)
	onKnob.setValue(VALUE)
	HOST.addKnob(onKnob)
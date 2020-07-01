import os
import nuke

def save():
	
	nkFile = getPath('compo', 'nk', 1, 0)
	nuke.scriptSaveAs(nkFile)

def writeC():
	
	nkFile = getPath('compoRender', '####.exr', 0, 1)
	print nkFile
	writeNode = nuke.createNode('Write', inpanel=True)
	writeNode['file'].setValue(nkFile)
	writeNode['create_directories'].setValue(1)
	writeNode['name'].setValue('PUBLISH')




def getPath(Type, ext, mkdir, local):

	aovPath = os.path.dirname(nuke.toNode('BEAUTY READ')['file'].getValue())+'/'

	if 'D:/' in aovPath and not local:
		aovPath = aovPath.replace('D:/', 'S:/')
	if 'S:/' in aovPath and local:
		aovPath = aovPath.replace('S:/', 'D:/')

	nkPath = aovPath.replace('render', Type)
	categoryList = ['FML', 'HD', 'LD']

	for category in categoryList:

		if category in nkPath:
			nkPath = nkPath.split(category)[0]

	if os.path.isdir(nkPath):
		versionsList = os.listdir(nkPath)
		if versionsList and versionsList != []:
			versionsList.sort()
			version = "%04d" %(int(versionsList[-1])+1)
		else:
			version = "0001"
	else:
		version = '0001'

	seq = nkPath.split('/')[-3]
	shot = nkPath.split('/')[-2]
	nkFileName = '{}_{}.{}'.format(seq, shot, ext)
	nkPath = nkPath+version+'/'

	nkFile = nkPath+nkFileName

	if not os.path.isdir(nkPath) and mkdir == 1:
		try:os.makedirs(nkPath)
		except:pass


	return nkFile
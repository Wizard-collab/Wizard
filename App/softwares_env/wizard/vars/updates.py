from wizard.vars import defaults

updates = dict()
updates['0.9.7.8-b'] = '''Version updates : 0.9.7.8-b

Version date : 2020-09-27

- Guerilla render graph publish and reference
- Guerilla light rig publish and reference
- Substance Painter save and maps export ( python )
- Make tx button on export manager
- Publish height map ( Substance Painter )
- Reference height map ( Guerilla Render )
- Publish sss map ( Substance Painter )
- Reference sss map ( Guerilla Render )
- Custom user shelf
- Scene graph as list
- Camera export set ( Maya )
- Export group creation auto ( Maya )
- Removed custom export extensions
- Wizard ui can be a classic windows ui ( Not only shutter )
- User can quickly add an asset to the shelf
- Removed WSD - Not stable
- Debug - First playblast appear
- Debug - References are no inherent to asset.software ( not asset.variant )
- Debug - Gray background on playblasts
- Debug - Missing icon on archive asset ui
- Debug - User not forced to add a profile image
- Debug - Adminisrator creation need a password
- Debug - Substance Painter settings ui
- Debug - Substance Painter init file updated
- Debug - Emails ( Now OAuth2 - Gmail )
- Debug - Server architecture modified
'''
updates['0.9.7.81-b'] = '''Version updates : 0.9.7.81-b

Version date : 2020-09-28

- Wizard API included
- Playblast can be done from 'camera' stage ( Not only camRig )
- Debug mode added
- Debug - Playsound now ignored if can't load sound
- Debug - When unpin, wizard stay on the current asset
- Debug - Removing the python module "pickle"
- Debug - Removed wsd ui section in project settings
- Debug - Changed the "add_to_shelf" option using the wizard API
- Debug - Scripts names in logging file and in logging stream
- Debug - No more new version query at openning
- Debug - Critical error on asset lauch and close ( str item was passed instead of QTreeWidgetItem )
- Debug - Cam export fixed when stage doesn't exists and when only cam is selected
- Debug - Substance wizard plugin
'''
updates['0.9.7.82-b'] = '''Version updates : 0.9.7.82-b

Version date : 2020-09-29

- Debug - Substance wizard plugin
'''
updates['0.9.7.83-b'] = '''Version updates : 0.9.7.83-b

Version date : 2020-09-30

Added a task progress bar in the main ui
- Debug - Nuke launch
- Debug - Set dress and set workflow ( No more name clash at layout publish )
'''
updates['0.9.7.84-b'] = '''Version updates : 0.9.7.84-b

Version date : 2020-10-01

- Debug - Auto hair ( maya + yeti added to pub_ext_dic )
- Debug - Grooming : Publish solved ( No more camRig_GRP asked )
'''
updates['0.9.7.85-b'] = '''Version updates : 0.9.7.85-b

Version date : 2020-10-01

- Debug - Debug Maya + Yeti ( No more maya yeti as defaults software )
'''
updates['0.9.7.86-b'] = '''Version updates : 0.9.7.86-b

Version date : 2020-10-04

- Added focal length on playblasts
- Added xp popups
- Maya imports are now automatic
- Added an "import all" button in Maya - Wizard shelf
- Debug - Debug Maya + Yeti ( No more maya yeti as defaults software )
- Debug - Pickle fail on software launch
- Debug - Screen capture of work version is now from the current screen
- Debug - Stage refresh on creation popups
- Debug - Project tree refresh is way faster
- Debug - Errors when creating a new project ( Related to a missing user asset context )
- Debug - Icons selection for wizard user shelf tool is now resizable
- Debug - Ui refreshing is way more clean
- Debug - Compil is way more clean
- Debug - No more updater.exe in the install
'''

updates['0.9.7.87-b'] = '''Version updates : 0.9.7.87-b

Version date : 2020-10-10

- Substance designer is now accessible from wizard
- Substance designer plugin ( Save and SBSAR exports )
- Clean API sctructure
- You can now merge files in wizard by drag and drop files in versions tab
- Stage information in reference list items
- Yeti - Abc workflow available
- Batch export - Refresh auto option for exports and playblasts
- You can now set prerolls and postrolls for shots
- Preroll and postroll button in Maya/Wizard shelf
- You can now playblast from the published camera of the shot in any Maya scene
- Updates history is now accessible
- Wizard now references all exported assets ( char_1_anim, char_2_anim, etc... )
- Debug - Maya + Yeti shelf icons are back !
- Debug - Wizard memorize the user current tab
- Debug - No needed category icons were appearing when refreshing tree
- Debug - Crash when cancelling version, playblast or export comment
- Debug - Tabs are not movable anymore
'''

updates['0.9.7.88-b'] = '''Version updates : 0.9.7.88-b

Version date : 2020-10-27

- New script editor
- New file viewer
- User open tickets information
- Wizard memorize the last tab
- Blender is now working with wizard ( save + )
- New wall appearance
- 4K screens wrong DPI solved 
- Wizard in now in 64-b
- Installer is on "program files" by default ( not x86 anymore )
- Debug - Refresh server on refresh ui
- Debug - Refresh user widget on refresh ui
- Debug - Init file relative path bug resolved
- Debug - Maya save doesn't override existing file ( increment instead ) - Only when wizard isn't openned
'''
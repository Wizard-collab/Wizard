import maya.cmds as cmds
from wizard.tools import log

logger = log.pipe_log(__name__)


def create_shader(shader_name, files_list):

    ai_surface = cmds.shadingNode('aiStandardSurface', asShader=True, n=shader_name)
    shading_group= cmds.sets(renderable=True,noSurfaceShader=True,empty=True)
    cmds.connectAttr('%s.outColor' %ai_surface ,'%s.surfaceShader' %shading_group)

    basecolor_list = []
    metalness_list = []
    roughness_list = []
    normal_list = []

    for file in files_list:
        if "BASECOLOR" in file.upper():
            basecolor_list.append(file)
        elif "METALNESS" in file.upper():
            metalness_list.append(file)
        elif "ROUGHNESS" in file.upper():
            roughness_list.append(file)
        elif "NORMAL" in file.upper():
            normal_list.append(file)

    if basecolor_list != []:
        add_basecolor(ai_surface, basecolor_list[0], shader_name)

    if metalness_list != []:
        add_metalness(ai_surface, metalness_list[0], shader_name)

    if roughness_list != []:
        add_roughness(ai_surface, roughness_list[0], shader_name)

    if normal_list != []:
        add_normal(ai_surface, normal_list[0], shader_name)


def add_basecolor(shader, file, shader_name):

    file_node=cmds.shadingNode("file",asTexture=True, n = "%s_baseColor" % shader_name)
    cmds.setAttr( '%s.fileTextureName' % file_node, file, type = "string")
    cmds.connectAttr('%s.outColor' %file_node,'%s.baseColor' %shader)
    cmds.setAttr('%s.uvTilingMode' %file_node, 3)


def add_metalness(shader, file, shader_name):

    file_node=cmds.shadingNode("file",asTexture=True, n = "%s_metalness" % shader_name)
    cmds.setAttr( '%s.fileTextureName' % file_node, file, type = "string")
    cmds.connectAttr('%s.outAlpha' %file_node,'%s.metalness' %shader)
    cmds.setAttr('%s.colorSpace' %file_node,'Raw', type='string')
    cmds.setAttr('%s.ignoreColorSpaceFileRules' %file_node, 1)
    cmds.setAttr('%s.alphaIsLuminance' %file_node, 1)
    cmds.setAttr('%s.uvTilingMode' %file_node, 3)

def add_roughness(shader, file, shader_name):

    file_node=cmds.shadingNode("file",asTexture=True, n = "%s_roughness" % shader_name)
    cmds.setAttr( '%s.fileTextureName' % file_node, file, type = "string")
    cmds.connectAttr('%s.outAlpha' %file_node,'%s.specularRoughness' %shader)
    cmds.setAttr('%s.colorSpace' %file_node,'Raw', type='string')
    cmds.setAttr('%s.ignoreColorSpaceFileRules' %file_node, 1)
    cmds.setAttr('%s.alphaIsLuminance' %file_node, 1)
    cmds.setAttr('%s.uvTilingMode' %file_node, 3)

def add_normal(shader, file, shader_name):

    bump2d_node = cmds.shadingNode("bump2d", asShader=True, n = "%s_bump_node" % shader_name)
    cmds.setAttr('%s.bumpInterp' %bump2d_node, 1)
    cmds.setAttr('%s.aiFlipR' %bump2d_node, 0)
    cmds.setAttr('%s.aiFlipG' %bump2d_node, 0)

    file_node=cmds.shadingNode("file", asTexture=True, n = "%s_normal" % shader_name)
    cmds.setAttr( '%s.fileTextureName' % file_node, file, type = "string")
    cmds.setAttr('%s.colorSpace' %file_node,'Raw', type='string')
    cmds.setAttr('%s.ignoreColorSpaceFileRules' %file_node, 1)
    cmds.setAttr('%s.alphaIsLuminance' %file_node, 0)
    cmds.setAttr('%s.uvTilingMode' %file_node, 3)

    cmds.connectAttr('%s.outAlpha' %file_node,'%s.bumpValue' %bump2d_node)

    cmds.connectAttr('%s.outNormal' %bump2d_node,'%s.normalCamera' %shader)
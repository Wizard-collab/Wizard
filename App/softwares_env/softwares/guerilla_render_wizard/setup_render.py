from guerilla import Document, Modifier, pynode, Node, Plug, Preferences
from wizard.asset import main as asset_core
from wizard.vars import defaults
from softwares.guerilla_render_wizard import reference_asset
from softwares.guerilla_render_wizard import init_scene
import os
from wizard.project import wall
from wizard.prefs.main import prefs

prefs = prefs()

class export():

    def __init__(self):

        self.asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
        self.render_pass_list = get_all_render_passes()
        self.file_pattern = "$L_$n_$o.$05f.$x"
        self.depth = 'half'
        self.extension = 'exr'
        self.shot_range = prefs.asset(self.asset).name.range

    def set_FML(self):
        init_scene.set_format()
        middle_frame = int(self.shot_range[0]) + int((int(self.shot_range[1]) - int(self.shot_range[0]))/2)
        f_range = '{},{},{}'.format(self.shot_range[0], middle_frame, self.shot_range[1])
        self.setup_export('FML', f_range)
        wall.wall().publish_event(self.asset)

    def set_LD(self):
        init_scene.set_format(half=True)
        f_range = '{}-{}'.format(self.shot_range[0], self.shot_range[1])
        self.setup_export('LD', f_range)
        wall.wall().publish_event(self.asset)

    def set_HD(self):
        init_scene.set_format()
        f_range = '{}-{}'.format(self.shot_range[0], self.shot_range[1])
        self.setup_export('HD', f_range)
        wall.wall().publish_event(self.asset)

    def setup_export(self, job_type, f_range):

        export_file = self.asset.export('{}_{}_{}'.format(self.asset.category, self.asset.name, self.asset.variant), from_asset=self.asset)
        export_path = os.path.split(export_file)[0]
        full_file = os.path.join(export_path, self.file_pattern)

        for rp in self.render_pass_list:
            rp.Depth.set(self.depth)
            rp.DisplayDriver.set(self.extension)
            rp.FileName.set(full_file)

        preferences_node = reference_asset.get_node_from_name('Preferences')
        preferences_node.RenderRange.set(f_range)

        job_name = '{}_{}_{}_{}_{}'.format(prefs.project_name.lower(),
                                        job_type,
                                        self.asset.category,
                                        self.asset.name,
                                        self.asset.variant)

        preferences_node.RenderfarmSequence.set(job_name)
        preferences_node.DeferredRibGen.set(True)

class helios_bridge():

    def __init__(self):

        self.asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
        self.pass_name = '{}_{}_RP'.format(self.asset.category, self.asset.name)
        self.main_layer_name = 'shading_layer'
        self.main_aov_name = 'main_Beauty'
        self.main_rg_name = 'RG_layering'

        self.tag_rg_node = "layering_All_tag"
        self.main_layer_rg_node = "{}_rg_node".format(self.main_layer_name)
        self.output_rg_node = "layering_Output_node"

        self.lighting_layer_name = 'lighting_layer'
        self.lighting_layer_rg_node = "{}_rg_node".format(self.lighting_layer_name)

        self.create_shot_rp()

    def create_shot_rp(self):

        delete_default_pass()
        
        if self.pass_name not in reference_asset.get_all_nodes():
            self.main_render_pass = create_render_pass(self.pass_name)
        else:
            self.main_render_pass = reference_asset.get_node_from_name(self.pass_name)

        
        if self.main_layer_name not in reference_asset.get_all_nodes():
            self.main_layer = create_new_layer(self.main_layer_name, self.main_render_pass)
        else:
           self.main_layer = reference_asset.get_node_from_name(self.main_layer_name)

        layering_rg = create_render_graph(self.main_rg_name)
        if layering_rg:
            self.fill_render_main_graph(layering_rg, self.main_layer)
            create_beauty_aov(self.main_aov_name, self.main_layer)


    def create_lighting_layer(self):
        if self.lighting_layer_name not in reference_asset.get_all_nodes():
            self.lighting_layer = create_new_layer(self.lighting_layer_name, self.main_render_pass)
        else:
           self.lighting_layer = reference_asset.get_node_from_name(self.lighting_layer_name)
        
        for light in get_all_lights():
            add_light_category(light)
            aov_name = 'lgt_{}'.format(light.getname())
            aov = create_new_aov(aov_name, self.lighting_layer, aov_name)
            aov.LightCategories.set(light.getname())
            aov.AcceptPath.set('All')
            aov.IgnorePath.set('Caustics')

        self.add_lighting_layer_to_rg(reference_asset.get_node_from_name(self.main_rg_name), self.lighting_layer)

    def fill_render_main_graph(self, rg, layer):
        tag1 = rg.loadfile('$(LIBRARY)/rendergraph/tag.gnode')
        tag1[0].Tag.set("All")
        tag1[0].rename(self.tag_rg_node)

        shading_layer = rg.loadfile("$(LIBRARY)/rendergraph/renderlayer.gnode")
        shading_layer[0].rename(self.main_layer_rg_node)
        shading_layer[0].Membership.set('layer:shading_layer')
        shading_layer[0].Input1.Plug.connect(tag1[0].Output1.Plug)

        out1 = rg.loadfile('$(LIBRARY)/rendergraph/output.gnode')
        out1[0].Input1.Plug.connect(shading_layer[0].Output1.Plug)
        out1[0].rename(self.output_rg_node)
        replace = 0

    def add_lighting_layer_to_rg(self, rg, layer):
        if self.lighting_layer_rg_node not in reference_asset.get_all_nodes():
            main_layer_rg_node = reference_asset.get_node_from_name(self.main_layer_rg_node)
            main_output_rg_node = reference_asset.get_node_from_name(self.output_rg_node)

            lighting_layer = rg.loadfile("$(LIBRARY)/rendergraph/renderlayer.gnode")
            lighting_layer[0].rename(self.lighting_layer_rg_node)
            lighting_layer[0].Membership.set('layer:{}'.format(layer.getname()))
            lighting_layer[0].Input1.Plug.connect(main_layer_rg_node.Output1.Plug)

            main_output_rg_node.Input1.Plug.disconnect(main_layer_rg_node.Output1.Plug)
            main_output_rg_node.Input1.Plug.connect(lighting_layer[0].Output1.Plug)

def delete_default_pass():
    with Modifier() as mod:
        if 'RenderPass' in reference_asset.get_all_nodes():
            mod.deletenode(reference_asset.get_node_from_name('RenderPass'))

def create_render_pass(name):
    with Modifier() as mod:
        render_pass = mod.createnode(name, type='RenderPass')
        mod.connect(render_pass.Width,Document().ProjectWidth)
        mod.connect(render_pass.Height,Document().ProjectHeight)
        mod.connect(render_pass.AspectRatio,Document().ProjectAspectRatio)
    return render_pass

def create_render_graph(name):
    if name not in reference_asset.get_all_nodes():
        render_graph = Node.create(name, 'RenderGraph')
        #rg.move(shaders_GRP)
    else:
        render_graph = None
    return render_graph

def create_new_layer(name, parent):
    with Modifier() as mod:
        layer = mod.createnode(name, type='RenderLayer', parent=parent)
    return layer


def create_beauty_aov(name, parent):
    aov = create_new_aov(name, parent)
    aov.PlugName.set('Beauty')
    return aov


def create_new_aov(name, parent, plug = None):
    with Modifier() as mod:
        if name not in reference_asset.get_all_nodes():
            aov = mod.createnode(name, type='LayerOut', parent=parent)
        else:
            aov = reference_asset.get_node_from_name(name)
        if plug:
            aov.PlugName.set(plug)
    return aov

def get_all_lights():
    lights_list = []
    for light in Document().children(recursive=True, type="Light"):
        lights_list.append(light)
    return lights_list

def get_all_render_passes():
    rp_list = []
    for rp in Document().children(recursive=True, type="RenderPass"):
        rp_list.append(rp)
    return rp_list

def add_light_category(light):
    light.Category.set(light.getname())

import_asset_script = '''# Import the asset main module to manipulate assets
from wizard.asset import main as asset_core
# Import the asset reference module to create references
from wizard.asset.reference import references
# Import the prefs main module to manipulate wizard datas
from wizard.prefs.main import prefs
# Import the scene module to interact with the UI
import scene

# Initialise the prefs module
prefs = prefs()
# Get the current asset using the "scene" module
current_asset = scene.current_asset()
# Convert this ASSET_STRING string to a wizard asset object
asset = asset_core.string_to_asset("ASSET_STRING")
# Get the default export asset of the reference asset
asset.export_asset = prefs.asset(asset).export_root.default_export_asset
# Get the last export version of the reference asset
asset.set_export_version()
# Create the reference
references(current_asset).add_reference(asset, 0, 1)
# Refresh the ui
scene.refresh_ui()'''
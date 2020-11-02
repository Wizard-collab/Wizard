from wizard.tools import log
from wizard.tools import utility as utils

logger = log.pipe_log(__name__)

def batch_asset_creation(asset, in_out):

	string_asset = utils.asset_to_string(asset)

	command = "import sys\n"
	command += "import os\n"
	command += "sys.path.append(os.path.abspath(''))\n\n"
	command += "from wizard.tools import utility as utils\n"
	command += "from wizard.asset import main as asset_core\n\n"
	command += f'asset = asset_core.string_to_asset("{string_asset}")\n'
	command += f'asset.create({in_out}, batch=1)\n'
	command += 'print("status:Done !")'

	file = utils.temp_file_from_command(command)
	return file
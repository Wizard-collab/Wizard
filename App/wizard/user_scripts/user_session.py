from wizard.tools import utility as utils
from wizard.tools import log
import importlib
import sys
import traceback

from wizard.prefs import user_scripts
user_scripts.user_scripts()

utils.session_file_from_command('')
import session

logger = log.pipe_log(__name__)

def execute_session_script(command):
	
	utils.session_file_from_command(command)

	try:
		importlib.reload(session)
	except:
		logger.warning(str(traceback.format_exc()))

	sys.stdout.flush()

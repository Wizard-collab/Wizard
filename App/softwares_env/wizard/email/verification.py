from wizard.tools import log
from wizard.email import main as send_email
import random

logger = log.pipe_log()

def confirm_email(user, email):
	temp_pass = random.randint(1000,1000).zfill(4)
	send_email.send_confirm(user, email, temp_pass)

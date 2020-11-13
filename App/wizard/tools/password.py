# coding: utf-8

import random
# Wizard variables modules
from wizard.email import main as send_email
# Wizard tools modules
from wizard.tools import log
import hashlib, binascii, os

# Create the main logger
logger = log.pipe_log(__name__)


def encrypt(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def decrypt(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def recover(user, email):
    new_pwd = str(random.randint(1000000, 10000000))
    encrypted = encrypt(new_pwd)
    send_email.send_password(email, user, new_pwd)
    return new_pwd

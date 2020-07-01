#! /usr/bin/python

import smtplib
from wizard.tools import log
import socket

logger = log.pipe_log()

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import traceback


def send_error(user, user_email, error, message):
    me = "wizard-support@leobrunel.com"
    send_list = []
    send_list.append(me)
    send_list.append(user_email)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = ' \U0001F6A7 {} - Error report\n'.format(user)
    msg['From'] = me
    msg['To'] = user_email

    # Create the body of the message (a plain-text and an HTML version).
    html = """\
	<html>
	  <head></head>
	  <body>
	    <p>Hi there {}!<br><br>
	       <b>You reported this error :</b><br>
	       <p style="background-color: #3C4150; color:white">{}</p><br>
	       <b>Attached with this message :</b><br>
	       {}<br><br>
	       Thanks for your report,<br>
	       I come back to you <b>as soon as possible</b>!
	       \U0001F596
	    </p>
	  </body>
	</html>
	""".format(user, error, message)
    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    send_email(me, send_list, msg)

def error_submit(user, error):
    me = "wizard-support@leobrunel.com"
    send_list = []
    send_list.append(me)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = ' \U0001F6A7 {} - Error auto submit\n'.format(user)
    msg['From'] = me
    msg['To'] = me

    # Create the body of the message (a plain-text and an HTML version).
    html = """\
    <html>
      <head></head>
      <body>
        <p>Error submit<br><br>
           <b>{} created this error :</b><br>
           <p style="background-color: #3C4150; color:white">{}</p><br>
        </p>
      </body>
    </html>
    """.format(user, error)
    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    send_email(me, send_list, msg)


def send_help(user, user_email, message):
    me = "wizard-support@leobrunel.com"
    send_list = []
    send_list.append(me)
    send_list.append(user_email)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = ' \U0001F4AC	 {} - Help request\n'.format(user)
    msg['From'] = me
    msg['To'] = user_email

    # Create the body of the message (a plain-text and an HTML version).
    html = """\
	<html>
	  <head></head>
	  <body>
	    <p>Hi there {}!<br><br>
	       <b>You sent this message to the support :</b><br>
	       {}<br><br>
	       Thanks for your request,<br>
	       I come back to you <b>as soon as possible</b> ! 
	       \U0001F596
	    </p>
	  </body>
	</html>
	""".format(user, message)
    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    send_email(me, send_list, msg)


def send_password(user_email, user, password):
    me = "wizard-support@leobrunel.com"
    send_list = []
    send_list.append(user_email)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = ' \U0001F511 {} - Your new wizard password\n'.format(user)
    msg['From'] = me
    msg['To'] = user_email

    # Create the body of the message (a plain-text and an HTML version).
    html = """\
	<html>
	  <head></head>
	  <body>
	    <p>Hi there {}!<br><br>
	       <b>You requested a new password, here it is :</b>
	       {}<br>
	       Please change and try <b>remember it</b> ! 
	       \U0001F60F
	    </p>
	  </body>
	</html>
	""".format(user, password)
    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    send_email(me, send_list, msg)


def send_confirm(user, email, verfication_pass, full_name):
    user_email = email
    me = "wizard-support@leobrunel.com"
    send_list = []
    send_list.append(user_email)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = ' \U0001F590	 {} - Welcome my new friend !\n'.format(full_name)
    msg['From'] = me
    msg['To'] = user_email

    # Create the body of the message (a plain-text and an HTML version).
    html = """\
	<html>
	  <head></head>
	  <body>
	    <p>Hi there {}!<br><br>
	       <b>Welcome to wizard, here is your confirmation pass :</b>
	       {}<br>
	       <b>Have fun ! </b>
	       \U0001F40D	
	    </p>
	  </body>
	</html>
	""".format(full_name, verfication_pass)
    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    send_email(me, send_list, msg)


def request_unlock(user, user_requesting, email, verfication_pass, asset):
    user_email = email
    me = "wizard-support@leobrunel.com"
    send_list = []
    send_list.append(user_email)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = ' \U0001F512	 {} request an unlock\n'.format(user_requesting)
    msg['From'] = me
    msg['To'] = user_email

    # Create the body of the message (a plain-text and an HTML version).
    html = """\
	<html>
	  <head></head>
	  <body>
	    <p>Hi there {}!<br><br>
	       <b>{} is requesting an asset ( {}-{}-{}-{}-{} ) unlock. Here is the confirmation pass :</b>
	       {}<br>
	       \U0001F40D	
	    </p>
	  </body>
	</html>
	""".format(user, user_requesting, asset.domain, asset.category, asset.name, asset.stage, asset.software,
               verfication_pass)
    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    send_email(me, send_list, msg)


def send_joke(user, joke):
    me = "wizard-support@leobrunel.com"
    send_list = []
    send_list.append(me)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = ' \U0001F693	 {} - Added a joke !\n'.format(user)
    msg['From'] = user
    msg['To'] = me

    # Create the body of the message (a plain-text and an HTML version).
    html = """\
	<html>
	  <head></head>
	  <body>
	    <p>New joke :<br><br>  
	       {}<br>
	    </p>
	  </body>
	</html>
	""".format(joke)
    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    send_email(me, send_list, msg)


def send_email(me, send_list, msg):
    try:
        # Send the message via local SMTP server.
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('wizard-support@leobrunel.com', "Tv8ams23061995")
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        for send in send_list:
            server.sendmail(me, send, msg.as_string().encode('utf8'))
        server.quit()
        logger.info("Email sent")
    except socket.gaierror:
        logger.error("Email : No internet connection")
    except:
        logger.critical(str(traceback.format_exc()))

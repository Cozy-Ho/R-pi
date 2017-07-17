# -*- coding: utf-8 -*-

import subprocess

def sendAutostartMail():
	import smtplib
	import string
	USER = 'kj2693119@gmail.com'
	PASS = 'Kangju1379/'
	TO = 'kj2693119@gmail.com'
	SUBJECT = '[R-PI] Autostart Mail'
	ip = subprocess.check_output("hostname -I", shell = True)
	TEXT = 'Autostart 메일 입니다. \nR-PI의 IP 주소는 다음과 같습니다.\n%s' %ip
#	print TEXT
	FROM = USER
	HOST = 'smtp.gmail.com:587'
	BODY = string.join((
		'From: %s' %FROM,
		'To: %s' %TO,
		'Subject: %s' %SUBJECT,
		'\r\n',
		TEXT,
		), '\r\n')

	server = smtplib.SMTP(HOST)
	server.starttls()
	server.login(USER, PASS)
	server.sendmail(FROM, TO, BODY)
	server.quit()

	print 'Sendded mail to %s.' %TO

if __name__ == "__main__":
	sendAutostartMail()


# -*- coding: utf-8 -*-

#공유기가 재부팅되거나 ip충돌로 외부ip주소가 바뀌어버리면 외부에서 접속할 방법이없다ㅠ
#그래서 주기적으로 외부ip주소를 뽑아 메일로 보내주는 프로그램을 만들었다.

import subprocess

def sendAutostartMail():
	import smtplib
	import string
	USER = 'kj2693119@gmail.com'
	PASS = 'Kangju1379/'
	TO = 'kj2693119@gmail.com'
	SUBJECT = '[R-PI] Autostart Mail'
	ip = subprocess.check_output("curl icanhazip.com", shell = True)
	TEXT = 'Autostart 메일 입니다. \nR-PI의 외부 IP 주소는 다음과 같습니다.\n%s' %ip
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


import RPi.GPIO as GPIO
import time,smtplib,datetime

#nums = ['6143776769@vtext.com']#,'<insertVerizonPhoneNum>@vtext.com']

def sendText(message, numbers):
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.ehlo()
    s.login('eakers1123@gmail.com','mpde qlny yeph bwmc')
    for n in numbers:
        s.sendmail('eakers1123@gmail.com',n,'Subject: '+message)


sendAlert('pi has booted up')

GPIO.setmode(GPIO.BCM)

#The pin that is currently hooked up
GPIO.setup(17,GPIO.IN)
input = GPIO.input(17)
closed = True
while True:

    year, month, day, hour, minute, second = time.strftime("%Y,%m,%d,%I,%M,%S").split(',')
    hour = str((int(hour)+7)%12)
    #t = year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second
    t = hour + ':' + minute
    
	#TODO get users on WiFi
	time.sleep(2)

	#TODO check time before doing anythin

	if GPIO.input(17):
        if not closed:
            print('closed')
            closed = True
			#TODO implement send alert
            sendAlert(t+' Front door closed')
            while GPIO.input(17):
                time.sleep(2)
    else:
        print('open')
        closed = False
        sendAlert(t+' Front door opened')
        while not GPIO.input(17):
            time.sleep(1)

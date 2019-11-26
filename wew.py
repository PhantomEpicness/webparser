from twilio.rest import Client
import time
def sendText(userInput="i feel empty"):
	accountSSID = 'ACe5c7e8602f7093eb54ec24f0a2da25ff'
	authToken = '0e5385500edf90d482a28fb7a35bc66e'
	
	twilioCli = Client(accountSSID, authToken)
	myTwilioNumber = '+15189074216'
	myCellPhone = '+18085907487'
	
	message = twilioCli.messages.create(
		body='my python app says '+userInput,
		from_ =myTwilioNumber,
		to=myCellPhone
		)
msg = input("what would you like to send?")
sendText(msg)

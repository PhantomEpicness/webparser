from twilio.rest import Client
import time
def sendText(userInput="i feel empty"):
	accountSSID = ''
	authToken = ''
	
	twilioCli = Client(accountSSID, authToken)
	myTwilioNumber = ''
	myCellPhone = ''
	
	message = twilioCli.messages.create(
		body='my python app says '+userInput,
		from_ =myTwilioNumber,
		to=myCellPhone
		)
msg = input("what would you like to send?")
sendText(msg)

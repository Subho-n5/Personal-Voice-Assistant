#!/usr/bin/env python3
import speech_recognition as sr
import os
import sys
from gtts import gTTS
from time import ctime

text = ""
reply = ""
r = sr.Recognizer()
mic = sr.Microphone(device_index=6)

def speak(reply):
	ts = gTTS(reply)
	ts.save('test.mp3')
	os.system("mpg321 test.mp3 -quiet")


while True : 
	with mic as source:
		r.adjust_for_ambient_noise(source)
		print('Say!')
		audio1 = r.listen(source)


	try:
		text = r.recognize_google(audio1)
	except sr.UnknownValueError:
		text = "Could not understand audio"
	except sr.RequestError as e:
		text = "Internet Issues: {0}".format(e)
	
	if "hello" in text or "hi" in text:
		speak("Hello") 

	elif "how are you" in text:
		speak("I am fine! How are you?")

	elif "can you help me" in text:
		speak("How can I help you !")

	elif "close" in text:
		speak("closing myself")
		break;

	elif "time" in text:
		speak(ctime())

	else:
		speak("I didn't get u")

	









#Credits to Arvind Periyasamy https://github.com/arvindindeed/RealTimeSpeechToText/blob/master/DemoRealTimeSpeechToTxt.py
import os
import time
import azure.cognitiveservices.speech as speechsdk
from tkinter import *
import tkinter as tk

timestr = time.strftime("%Y%m%d-%H%M%S")
print (timestr)
filepath = r"output.txt"+timestr+".txt"
print (filepath)
f = open(filepath, 'a', buffering=1)
appHeight = 150
padding = 20
labelText = NONE

def recognizing(args):
    global labelText
    labelText.set(args.result.text)

def recognized(args):
    global f
    if args.result.text.strip() != '':
        print(args.result.text + "\n")
        f.write(args.result.text + "\n")

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Say something...")

speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

speech_recognizer.recognizing.connect(recognizing)
speech_recognizer.recognized.connect(recognized)
speech_recognizer.start_continuous_recognition()

 #Let the program lasts for 100 seconds. This time range can be changed to when the user wanna stop use this program

time.sleep(500)           



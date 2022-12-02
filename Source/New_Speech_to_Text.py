#Credits to Arvind Periyasamy https://github.com/arvindindeed/RealTimeSpeechToText/blob/master/DemoRealTimeSpeechToTxt.py
import os
import time
import azure.cognitiveservices.speech as speechsdk
from tkinter import *
import tkinter as tk
import sys
from OneDriveapi.Files_to_OneDrive import uploadToOneDrive

def realtime():
    speech_config = speechsdk.SpeechConfig(subscription="fc419cfd9f294afca49dc99a8aa7300a", region="centralus")
    #speech_config = speechsdk.SpeechConfig(subscription=os.environ.get(''), region=os.environ.get('SPEECH_REGION'))
    # Creates a recognizer with the given settings
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print (timestr)
    filepath = r"output.txt"+timestr+".txt"
    print (filepath)
    f = open(filepath, 'a', buffering=1)
    appHeight = 150
    padding = 20
    labelText = NONE
    print("The speech lasts for (seconds):" )
    recognizingTime = input()
    speech_config = speechsdk.SpeechConfig(subscription="fc419cfd9f294afca49dc99a8aa7300a", region="centralus")
    #speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('\nSESSION STOPPED {}'.format(evt)))
    speech_recognizer.recognizing.connect(lambda evt: print('\n{}'.format(evt.result.text)))
    speech_recognizer.recognizing.connect(lambda evt: f.write('\n{}'.format(evt.result.text)))
    speech_recognizer.start_continuous_recognition()

    #Let the program lasts for the amount of time entered in seconds. This time range can be changed to when the user wanna stop use this program
    time.sleep(int(recognizingTime))
    speech_recognizer.stop_continuous_recognition()

    speech_recognizer.session_started.disconnect_all()
    speech_recognizer.recognized.disconnect_all()
    speech_recognizer.session_stopped.disconnect_all()
 

def from_file():
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    
    # Creates a recognizer with the given settings
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print (timestr)
    filepath = r"output.txt"+timestr+".txt"
    print (filepath)
    f = open(filepath, 'a', buffering=1)
    appHeight = 150
    padding = 20
    labelText = NONE
    print("Enter the filepath with file type name: ")
    inputFile = input()
    audio_input = speechsdk.AudioConfig(filename= inputFile)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    done = False

    def stop_cb(evt):
        """callback that stops continuous recognition upon receiving an event `evt`"""
        print('CLOSING on {}'.format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    all_results = []
    def handle_final_result(evt):
        all_results.append(evt.result.text)

    speech_recognizer.recognized.connect(handle_final_result)
    # Connect callbacks to the events fired by the speech recognizer
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.recognized.connect(lambda evt: f.write('\n{}'.format(evt.result.text)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)


# # Creates an instance of a speech config with specified subscription key and service region.
# # Replace with your own subscription key and service region (e.g., "westus").
# speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
# # Creates a recognizer with the given settings
# speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
# timestr = time.strftime("%Y%m%d-%H%M%S")
# print (timestr)
# filepath = r"output.txt"+timestr+".txt"
# print (filepath)
# f = open(filepath, 'a', buffering=1)
# appHeight = 150
# padding = 20
# labelText = NONE

# def recognizing(args):
#     global labelText
#     labelText.set(args.result.text)

# def recognized(args):
#     global f
#     if args.result.text.strip() != '':
#         print(args.result.text + "\n")
#         f.write(args.result.text + "\n")
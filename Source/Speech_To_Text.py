#Credits to Arvind Periyasamy https://github.com/arvindindeed/RealTimeSpeechToText/blob/master/DemoRealTimeSpeechToTxt.py
import os
import time
import azure.cognitiveservices.speech as speechsdk
from tkinter import *
import tkinter as tk
import sys
from time import sleep
import textwrap 
from os.path import exists
#from OneDriveapi.Files_to_OneDrive import uploadToOneDrive
from OneDriveUpload import OneDriveUpload


def realtime():
    if (exists("../OutputFiles/TranslatedSpeech.txt")):
        os.remove("../OutputFiles/TranslatedSpeech.txt")
    # speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_config = speechsdk.SpeechConfig(subscription="fc419cfd9f294afca49dc99a8aa7300a", region="centralus")
    # Creates a recognizer with the given settings
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print (timestr)
    #filepath = r"output.txt"+timestr+".txt"
    #print (filepath)
    #f = open(filepath, 'a', buffering=1)
    f = open("../OutputFiles/TranslatedSpeech.txt", 'w', buffering=1)    
    appHeight = 150
    padding = 20
    labelText = NONE
    print("The speech lasts for (seconds):" )
    recognizingTime = input()
    print("")

    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED')) # {}'.format(evt)))
    #print(end='\x1b[2k')
    speech_recognizer.recognizing.connect(lambda evt: print(textwrap.fill(format(evt.result.text) + "  ", width = 180),end='\r', flush=True))
    # speech_recognizer.recognizing.connect(lambda evt:sys.stdout.write("\r{}".format(evt.result.text)))
    # sys.stdout.flush()
    # sleep(1)
    speech_recognizer.recognized.connect(lambda evt: f.write('\n{}'.format(evt.result.text)))
    speech_recognizer.session_stopped.connect(lambda evt: print('\nSESSION ENDED')) #.format(evt)))
    speech_recognizer.start_continuous_recognition()

    #Let the program lasts for the amount of time entered in seconds. This time range can be changed to when the user wanna stop use this program
    time.sleep(int(recognizingTime))
    speech_recognizer.stop_continuous_recognition()

    speech_recognizer.session_started.disconnect_all()
    speech_recognizer.recognized.disconnect_all()
    speech_recognizer.session_stopped.disconnect_all()

    print("File was successfully converted!\n")
    OneDriveUpload("TranslatedSpeech.txt")
 

def from_file():
    if (exists("../OutputFiles/TranslatedAudio.txt")):
        os.remove("../OutputFiles/TranslatedAudio.txt")
    #speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_config = speechsdk.SpeechConfig(subscription="fc419cfd9f294afca49dc99a8aa7300a", region="centralus")

    # Creates a recognizer with the given settings
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print (timestr)
    #filepath = r"../OutputFiles/TranslatedAudio.txt"+timestr+".txt"
    #print (filepath)
    f = open("../OutputFiles/TranslatedAudio.txt", 'w', buffering=1)
    appHeight = 150
    padding = 20
    labelText = NONE
    print("Enter the filepath with file type name: ")
    inputFile = input()
    audio_input = speechsdk.AudioConfig(filename= "../Source/" + inputFile)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    done = False

    def stop_cb(evt):
        """callback that stops continuous recognition upon receiving an event `evt`"""
        ##print('CLOSING on {}'.format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    all_results = []
    def handle_final_result(evt):
        all_results.append(evt.result.text)

    speech_recognizer.recognized.connect(handle_final_result)
    # Connect callbacks to the events fired by the speech recognizer
    speech_recognizer.session_started.connect(lambda evt: print('CONVERSION STARTED')) #: {}'.format(evt)))
    speech_recognizer.recognized.connect(lambda evt: f.write('\n{}'.format(evt.result.text)))
    speech_recognizer.session_stopped.connect(lambda evt: print('CONVERSION ENDED')) # {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print("")) #print('CANCELED {}'.format(evt)))
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)

    print("File was successfully converted!\n")
    OneDriveUpload("TranslatedAudio.txt")
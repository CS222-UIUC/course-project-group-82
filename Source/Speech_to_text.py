import os
import requests
import msal
from msal import PublicClientApplication
import speech_recognition as sr
class speech_to_text ():
    r = sr.Recognizer()
    with sr.Microphone() as source, open('output.txt','w') as f:
        print("Listening...")
        r.energy_threshold = 10000 
        r.pause_threshold = 2;                                              # In order to allow                                      
        while 1:
            audio = r.listen(source, timeout= 3)                            # Allow Intermittent for 5 seconds with silence.Or it will terminate.
            ##
            try: 
                text = r.recognize_google(audio) 
                print('{}'.format(text))                                    # Print to console
                print('{}'.format(text), file = f)                          # Print to text file
            except:
                print("Oh no. Try again")                                   # Print out when the input is not recognizable


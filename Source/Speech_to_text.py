import os
import requests
import msal
from msal import PublicClientApplication
import speech_recognition as sr
class speech_to_text ():
    r = sr.Recognizer()
    with sr.Microphone() as source, open('output.txt','w') as f:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration = 0.4)                  # Wait for 0.4 seconds to recognize the background noise
        r.pause_threshold = 2;                                              # It allows pauses 2 seconds during each phrases                                      
        while 1:
            audio = r.listen(source, timeout= 3)                            # Allow Intermittent for 3 seconds with silence.Or it will terminate.
            ##
            try: 
                text = r.recognize_google(audio) 
                print('{}'.format(text))                                    # Print to console
                print('{}'.format(text), file = f)                          # Print to text file
            except:
                print("Oh no. Try again")                                   # Print out when the input is not recognizable


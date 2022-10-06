#Add waiting period that allows speaker to stop for a while. 

#Export the output to text file
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source, open('output.txt','w') as f:
    print("Listening...")
    while 1:
        audio = r.listen(source,timeout=10, phrase_time_limit=10)       # Allow Intermittent for 10 seconds.Or it will terminate.
        ##
        try: 
            text = r.recognize_google(audio) 
            print('{}'.format(text))                                    #print to console
            print('{}'.format(text), file = f)                          #print to text file
        except:
            print("Oh no. Try again")                                   # print out when the input is not recognizable
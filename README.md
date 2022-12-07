# course-project-group-82
course-project-group-82 created by GitHub Classroom

Alexis Serrano, Huiyao Liang, Sankar Gopalkrishna, Praneeth Rangamudri

# Introduction:

Attending in-person lectures can be challenging for students with a hearing impairment, vision impairment, or don’t speak English as their first language. The Translatify app helps users convert live speech and audio files to text, as well as other functionalities to convert text files and text inputs to a desired language. Not only does the app display the translations and create translated files, but users have the option to upload files to Microsoft OneDrive to store files in a database for later references. 

# Instructions: 

Navigate a text editor or Integrated Development Environment (IDE) to run the program
The group uses and suggests Microsoft Visual Studio Code:
Download link: https://code.visualstudio.com/download

In the terminal, type the following command: 

    “git clone https://github.com/CS222-UIUC/course-project-group-82.git”
    
This will download the program (and all required files) to run the app on your computer

In the terminal, install python modules: 

    “pip install msal” - Microsoft Graph API
    “pip install googletrans” - Google Translate API
    “pip install azure-cognitiveservices-speech” - Azure Cognitive Services API

To get the transcription workable, the user should go through the following document to get Azure configuration done. Create a Cognitive Services resource in the Azure portal - Azure Cognitive Services | Microsoft Learn

Go to the “Text_Main.py” file and run the file

    (In terminal) - “python3 Text_Main.py”
    (in VSCode) - Click the “▷” button with the “Text_Main.py” open

Follow the instructions that appear on the console 

# Technical Architecture (Function Descriptions):
def main():
The main() function takes input from the user to determine whether the user wants to perform one of the four functions (Speech-to-text, Audio-to-text, Text Input-to-Text, or Text File-to-Text). This function calls realTime(), fromFile(), inputToText(), or fileToText() depending on the user input. After the specific function is called and performs the specific task, the main() function will ask the user if they want to translate another file. Depending on the input, the main() function is called again. 

Main() is written in Python and written by Jenny and Alexis

def OneDriveUpload():
The OneDriveUpload() function takes input from the user to determine whether the file with the translation should be uploaded to OneDrive. If the user proceeds to upload the file to OneDrive (by typing ‘y’ as input), the OneDriveUpload() function will call uploadToOneDrive() to begin the process of accessing a user’s OneDrive account and uploading the specific file.

OneDriveUpload() is written in Python and written by Alexis. Function uses Microsoft Graph API.

def uploadToOneDrive(path):
The uploadToOneDrive() function is the main function that opens OneDrive on a web browser, accesses the user’s OneDrive account, and uploads the file (generated from one of the four functions) to the OneDrive database. This function calls generate_access_token() to generate a code for a user to connect their OneDrive account with our program. Once a code is generated, the function opens a default web browser on the user’s computer and opens a link to type the code. This prompts the user to login into Microsoft OneDrive. The function uses the passed parameter “path” (which is a string) to access the file that will be uploaded.

uploadToOneDrive() is written in Python and written by Alexis. Function uses Microsoft Graph API.

def generate_access_token(app_id, scopes):
The generate_access_token() function creates a code that a user inputs to Microsoft OneDrive, so the user grants access to the program to upload files to their OneDrive account. The function will also store the account for later uploads (i.e. the user does not have to repeat the login process multiple times). This function returns a string that is the code. Its parameters (“app_id”, “scopes”) represent the program so the generated code is specifically for our program. 

uploadToOneDrive() is written in Python and written by Alexis. Function uses Microsoft Graph API.

def translateText(toTranslate, fileTo, chosenLanguage):
This function takes in text that the user wants to be translated as well as the user’s desired language for the text to be translated into. “fileTo” represents where the output file will be saved. The function first detects the language within the text so that it knows from what language it’s being translated from. The chosenLanguage is converted into a key representing the translated language. This small conversion is needed since the translate() built in function (that translates the text) from the google trans module uses a key representing a language. 

translateText(toTranslate, fileTo, chosenLanguage) is written in Python and written by Praneeth and Sankar. Function uses Google Translate API. 

def translateFile(toTranslateFile, fileTo, chooseLanguage):
This function is similar to translateText() except it takes in a file to be translated. The translateFile() function will open the specified file and access each line. This function will call translateText() for each line in the file. It will pass the current line, fileTo, and choosenLanguage as parameters to translateText(). For the translateFile() function, “toTranslate'' is the file being translated, “fileTo'' is the file name containing the translation, and “choosenLanguage” is the desired language a user wants to translate the file to. After the translation, it provides the users with a preview of the translated file by printing each line. 

translateFile(toTranslateFile, fileTo, chooseLanguage) is written in Python and written by Praneeth and Sankar. Function uses Google Translate API. 

def inputToText():
When the user decides that they want to type in text that they want to translate, within Translation_Main.py, the function inputToText() is called. The function starts off by asking in the text the user wants to type in. Then it asks the language the user wants the text to be translated into. Finally it translates the text and asks the user if he or she wants the file to be saved. This function creates the file “TranslateText.txt” file.

inputToText() is written in Python and written by Praneeth and Sankar. Function uses Google Translate API. 

def fileToText():
Now suppose if the user wanted to enter in a text file that they then wanted to be translated into, then this function would be called. The function starts off by asking the user to enter the file that they want to be translated into as well as the language. Then it asks the user for the language for the file to be translated into. After that it asks the user to sign into one drive to save the output file. This function creates the file “TranslateFilet.txt” file. 

fileToText() is written in Python and written by Praneeth and Sankar. Function uses Google Translate API. 

def realTime():
This function uses LiveSpeech API for Microsoft Azure Cognitive Service. It transcribes the live speech to text and is stored in a text file with the exact time(dates with seconds) when the speech is recorded.

def fromFile():

This function uses LiveSpeech API for Microsoft Azure Cognitive Service. It transcripts the wmv. Audio file to text and stored in text file with the exact time(dates with seconds) when the audio file is needed to be transcribed.

# Member Roles

Alexis - Worked on user interaction and implementing the Microsoft Graph API to access OneDrive within the program

Jenny - Worked on the realTime() function and fromFile() function to transcribe live speech or audio file to text file.

Praneeth - Worked on creating test cases for different words/phrases to ensure translation using the Google Translate API works. Also worked on creating the file that takes in input from the user or a file and translates it. 

Sankar - Worked on the text translation using the Google Translate API. Created functions to let the user decide the resulting language, input text in either string or file format, and easily decide the desired language.


from OneDriveapi.Files_to_OneDrive import uploadToOneDrive

def OneDriveUpload(textFile):
    input_upload = input("Do you want to save this file to OneDrive? y - Yes, n - No ")
    print("")
    if (input_upload == "y"):
        print("You will be redirected to sign in to Microsoft OneDrive.\n" + 
        "Type the generated code and follow the instructions.\n" + "This is a one-time procedure.\n" + 
        "If you already signed in to OneDrive. Type y.\n")
        response = input("Proceed?\n y - Yes, n - No: ")
        print("")
        if (response == "y"):
            uploadToOneDrive("../OutputFiles/" + textFile)
            print("Successfully uploaded file!")
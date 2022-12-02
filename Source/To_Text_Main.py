import New_Speech_to_Text as s
import Text_main as t
def main():
    print
    mode = input("Please choose the type of file you want to translate: " + "\n" + "s - speech, a - audio, t - text file, i - input text, x - end program: ")
    if (mode == 's' or mode == 'a' or mode == 't' or mode == 'i'):
        if mode == "s":
            s.realtime()
        elif mode == "a":
            s.from_file()
        elif mode == "i":
            t.inputToText()
        elif mode == "t":
            t.fileToText()
        response = input("Would you like to translate another file: " + "\n" + "y - yes, n - no: ")
        if (response == "y"):
            main()
    else :
        print("Program ended")
main()
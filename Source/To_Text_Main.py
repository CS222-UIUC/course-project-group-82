import New_Speech_to_Text as s
def main():
    print
    mode = input("please enter the mode you want to chose:")
    if mode == "realtime":
        s.realtime()
    elif mode == "audiofile":
        s.from_file()
    else:
        print("could not recognize")
main()
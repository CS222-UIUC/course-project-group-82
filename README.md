# course-project-group-82
course-project-group-82 created by GitHub Classroom

Authors: Alexis Serrano, Sankar Gopalkrishna, Praneeth Rangamudri, Huiyao Liang

Overview:
Students sometimes have a hard time understanding an instructor, have an audio impairment, or prefer to read than listen, or vice versa. Our program will accommodate students in in-person and online lectures as they can access a live translation of verbal speech to text, text to text, or video to text.

Instructions:
    Install Libraries:
        pip install speechrecognition
        pip install pyaudio
        pip install googletrans
    While program is listening to microphone it will print out in quotations, 'listening'. This tells the user to begin speaking to the microphone. As the speaking occurs, the program will display the text for the words being spoken on the screen. In addition, there will afterwards be an option to translate this result into different languages. If the environment is too loud to hear properly, or the words were unintelligible, the program will display on screen, 'Oh no!. Try again.'.

Troubleshooting Instructions:  
    If the install of googletrans causes a path issue, then do this:
        pip3 uninstall google trans
        pip3 install googletrans=3.1.0a0
        
 Demo of Live transcripting
    


https://user-images.githubusercontent.com/90361843/200074795-271e1dab-0bbd-44b5-81dd-0467cad71e0a.mp4


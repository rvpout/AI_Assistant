import speech_recognition as speech
import pyttsx3
import pywhatkit
import datetime
import wikipedia
#import pyjokes

listener = speech.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
text = "Hey buddy, how can I help"
text2 = "Is there something else you want me to do?"

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk(text)    

def take_command():
    try:
        with speech.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)
            
    except:
        pass
    return command

def run_AI():
    command = take_command()
    if "play" in command:
        song = command.replace("play", "")
        talk("Playing song " + song)
        pywhatkit.playonyt(song)
        talk(text2)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("Hey buddy, the clock is " + time)
        talk(text2)

    elif "search" in command:
        search = command.replace("search", "")
        talk("Hey buddy here is your search about " + search)
        search = pywhatkit.search(search)
        talk(text2)

    elif "what do you know about" in command:
        Wikipedia = command.replace("what do you know about", "")
        info = wikipedia.summary(Wikipedia, 1)
        talk(info)
        talk(text2)

    elif "how are you doing" in command:
        talk("I am doing amazing, thank you for asking")
        talk(text2)

    #elif "joke" in command:
     #   talk(pyjokes.get_joke())
    #    talk(text2)
    
    else:
        talk("Sorry, I am deaf what did you say")

while True:
    run_AI()
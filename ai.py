#import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to recognize and respond to voice commands
def recognize_speech():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

        # Use the Google Speech Recognition API to recognize the audio
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)

            # Use the text-to-speech engine to respond to the command
            engine.say("You said: " + text)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Sorry, I could not understand your command")
            engine.say("Sorry, I could not understand your command")
            engine.runAndWait()

        except sr.RequestError as e:
            print("Could not request results from the Google Speech Recognition service; {0}".format(e))
            engine.say("Could not request results from the Google Speech Recognition service")
            engine.runAndWait()

# Call the recognize_speech function in a loop to listen for commands
while True:
    recognize_speech()

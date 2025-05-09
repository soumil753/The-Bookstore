import win32com.client
import speech_recognition as sr

speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak("Hello, world!")

while True:
    print("Enter the text you want to convert to speech:")
    n = input()
    speaker.speak(n)
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

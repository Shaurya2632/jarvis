import speech_recognition as sr
from src.speak import speak
from src.agent import Agent

def run():
    recognizer = sr.Recognizer()
    agent = Agent()

    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio, language="en-in")
            response, should_exit = agent.handle(query)

            print("Jarvis:", response)
            speak(response)

            if should_exit:
                break

        except Exception:
            speak("Sorry, I did not understand.")

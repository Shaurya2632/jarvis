import speech_recognition as sr
from src.speak import speak
from src.agent import Agent

def run():
    recognizer = sr.Recognizer()
    agent = Agent()

    print("Jarvis is ready...")

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=5
            )

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-in")
            print("You:", query)

            response, should_exit = agent.handle(query)

            print("Jarvis:", response)
            speak(response)

            if should_exit:
                break

        except sr.WaitTimeoutError:
            print("Listening timed out.")
            continue

        except Exception as e:
            print("Error:", e)
            speak("Sorry, I did not understand.")

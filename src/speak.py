import win32com.client

def speak(message="", rate=0):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Rate = rate
    speaker.Speak(message)

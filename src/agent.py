import datetime
import webbrowser
import pyjokes

from src.utils import is_contains, is_contains_any, safe_eval
from src.model import Model

class Agent:
    def __init__(self):
        self.model = Model()

    def handle(self, query):
        query = query.lower()
        classification = self.model.classify(query)

        if "exit" in classification:
            return "Exiting Jarvis", True

        if classification[0].startswith("realtime"):
            search_query = classification[0].replace("realtime", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            return "Searching online", False

        if classification[0].startswith("open"):
            website = classification[0].replace("open", "").strip()
            webbrowser.open(f"https://www.{website}.com")
            return f"Opening {website}", False

        if is_contains(query, "tell", "joke"):
            return pyjokes.get_joke(), False

        if is_contains_any(query, "your name"):
            return "My name is Jarvis", False

        if "time" in query:
            return datetime.datetime.now().strftime("%I:%M:%S"), False

        if "date" in query:
            return datetime.datetime.now().strftime("%d %B %Y"), False

        try:
            result = safe_eval(query)
            return f"{query} = {round(result,2)}", False
        except:
            pass

        return "Please ask a valid query", False

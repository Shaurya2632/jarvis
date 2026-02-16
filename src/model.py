import cohere
from dotenv import dotenv_values

class Model:
    def __init__(self):
        env = dotenv_values(".env")
        api_key = env.get("COHERE_KEY")

        self.co = cohere.Client(api_key)
        self.preamble = self._build_preamble()

    def _build_preamble(self):
        return """
You are a decision classification model.
Only classify queries.

Categories:
- general (query)
- realtime (query)
- open (app/website)
- play (song)
- google search (topic)
- youtube search (topic)
- exit

Never answer. Only classify.
"""

    def classify(self, prompt):
        stream = self.co.chat_stream(
            model="command-r-plus",
            message=prompt,
            temperature=0.3,
            preamble=self.preamble
        )

        response = ""
        for event in stream:
            if event.event_type == "text-generation":
                response += event.text

        response = response.strip().replace("\n", "")
        return [r.strip() for r in response.split(",")]

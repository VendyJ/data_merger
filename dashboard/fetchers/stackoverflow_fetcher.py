import requests
from dashboard.services.granite_connector import GraniteDBConnector

class StackOverflowFetcher:
    BASE_URL = "https://api.stackexchange.com/2.3/questions"

    def __init__(self):
        self.db = GraniteDBConnector()

    def fetch_python_questions(self, tag="django"):
        """
        Stáhne otázky ze StackOverflow podle tagu (default: 'django')
        a uloží je do databáze.
        """
        params = {
            "order": "desc",
            "sort": "votes",
            "tagged": tag,
            "site": "stackoverflow",
            "pagesize": 5  # jen 5 nejlepších pro demo
        }

        response = requests.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            for q in data["items"]:
                title = q["title"]
                score = q["score"]
                link = q["link"]
                self.db.save_question(title, score, link)
            return True
        else:
            print("Chyba při volání StackOverflow API:", response.status_code)
            return False


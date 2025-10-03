import requests
from dashboard.services.granite_connector import GraniteDBConnector

class GitHubFetcher:
    BASE_URL = "https://api.github.com/search/repositories"

    def __init__(self):
        self.db = GraniteDBConnector()

    def fetch_python_repos(self, query="django"):
        """
        Stáhne repozitáře z GitHubu podle dotazu (default: 'django')
        a uloží je do databáze.
        """
        params = {
            "q": f"{query} language:python",
            "sort": "stars",
            "order": "desc",
            "per_page": 5  # jen 5 nejlepších pro demo
        }

        response = requests.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            for repo in data["items"]:
                name = repo["name"]
                stars = repo["stargazers_count"]
                url = repo["html_url"]
                self.db.save_repo(name, stars, url)
            return True
        else:
            print("Chyba při volání GitHub API:", response.status_code)
            return False

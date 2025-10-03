from dashboard.models import Repo, Question

class GraniteDBConnector:
    # Uložení repozitáře do databáze
    def save_repo(self, name, stars, url):
        Repo.objects.create(name=name, stars=stars, url=url)

    # Uložení otázky do databáze
    def save_question(self, title, score, link):
        Question.objects.create(title=title, score=score, link=link)

    # Načtení všeho z DB
    def get_all(self):
        return {
            "repos": Repo.objects.all(),
            "questions": Question.objects.all()
        }

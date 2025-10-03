from django.db import models

# Model pro GitHub repozitáře
class Repo(models.Model):
    name = models.CharField(max_length=200)  # název repozitáře
    stars = models.IntegerField()            # počet hvězdiček
    url = models.URLField()                  # odkaz na GitHub
    fetched_at = models.DateTimeField(auto_now_add=True)  # kdy jsme data stáhli

# Model pro StackOverflow otázky
class Question(models.Model):
    title = models.CharField(max_length=300) # titulek otázky
    score = models.IntegerField()            # skóre otázky
    link = models.URLField()                 # odkaz na otázku
    fetched_at = models.DateTimeField(auto_now_add=True)
from django.shortcuts import render
from .models import Repo, Question

def dashboard_view(request):
    # Načteme všechna data z DB
    repos = Repo.objects.all()
    questions = Question.objects.all()

    # Vrátíme je do šablony
    return render(request, "dashboard.html", {
        "repos": repos,
        "questions": questions
    })

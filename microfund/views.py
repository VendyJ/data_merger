from django.shortcuts import render, redirect
from .models import Request, Student
from .forms import RequestForm


def dashboard_view(request):
    requests = Request.objects.all()
    return render(request, "microfund/dashboard.html", {"requests": requests} )

def add_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            #Prozatím přiřadíme prvního studenta (jen test)
            new_request.student = Student.objects.first()
            new_request.save()
            return redirect("dashboard")
    else:
        form = RequestForm()
    return render(request, "microfund/add_request.html", {"form": form})
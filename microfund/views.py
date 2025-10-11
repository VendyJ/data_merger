from django.shortcuts import render, redirect, get_object_or_404
from .models import Request, Student
from .forms import RequestForm, DonateForm


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

def donate(request, id):
    # Najdeme konkrétní žádost podle ID (nebo vrátíme 404, pokud neexistuje)
    req = get_object_or_404(Request, id=id)

    # Přičteme částku, kterou dárce zadal
    if request.method == "POST":
        form = DonateForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data["amount"]
            req.donor_amount += amount
            req.save()
            return redirect("dashboard")
    else:
        form = DonateForm()

    return render(request, "microfund/donate.html", {"form": form, "req": req})

    # Uložíme změnu do databáze
    req.save()

    return redirect("dashboard")
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Request, Student
from .forms import RequestForm, DonateForm




def dashboard_view(request):
    requests = Request.objects.all()
    return render(request, "microfund/dashboard.html", {"requests": requests} )
 
 # REACT začátky
def api_requests(request):
    requests = Request.objects.all().values("id", "name", "description", "cash_amount", "donor_amount", "status")
    return JsonResponse(list(requests), safe=False)

@csrf_exempt # vypneme CSRF ochranu (protože budeme testovat přes POST)
@require_http_methods(["POST"])
def api_add_request(request):
    try:
        data = json.loads(request.body) # načteme JSON z těla požadavku

        student_id = data.get("student_id")

        # Ověříme, že student existuje
        student = Student.objects.filter(id=student_id).first()
        if not student:
            return JsonResponse({
                "success": False,
                "error": f"Student s ID {student_id} neexistuje."
            }, status=400)

        # vytvoření nové žádosti
        new_request = Request.objects.create(
            student=student,
            name=data.get("name"),
            description=data.get("description"),
            cash_amount=data.get("cash_amount"),
            donor_amount=data.get("donor_amount", 0),
            status=data.get("status", "active"),
        )

        return JsonResponse({
            "success": True,
            "message": "Žádost byla úspěšně vytvořena.",
            "request_id": new_request.id
        })
    
    except Exception as e:
        return JsonResponse({
            "success": False,
            "error": str(e)
        }, status=400)
    
@csrf_exempt # vypne ochranu proti CSRF, ať to Postman pustí
@require_http_methods(["POST"]) # povolíme jen POST
def api_donate(request):
    try:
        # načteme JSON z těla požadavku
        data = json.loads(request.body)

        # zkusíme získat request_id a částku
        request_id = data.get("request_id")
        amount = data.get("amount", 0)

        # najdeme konkrétní žádost podle ID (nebo vrátíme chybu)
        req = Request.objects.filter(id=request_id).first()
        if not req:
            return JsonResponse({
                "success": False,
                "error": f"Žádost s ID {request_id} neexistuje."
            }, status=404)
        
        # přičteme částku
        req.donor_amount += amount
        req.save()

        # odpověď
        return JsonResponse({
            "success": True,
            "message": f"Přidáno {amount} Kč.",
            "new_total": req.donor_amount
        })
    
    except Exception as e:
        # fallback, kdyby se něco pokazilo
        return JsonResponse({
            "success": False,
            "error": str(e)
        }, status=400)
 
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
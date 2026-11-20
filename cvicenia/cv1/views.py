from django.shortcuts import render

def cv1_index(request):
    kontext = {
        "meno": "Samuel"
    }
    return render(request, "cv1/cv1_index.html", kontext)

def cv1_obchod(request):
    data = [
        {"nazov": "Jablko", "cena": 0.99, "skryte": False},
        {"nazov": "Chlieb", "cena": 2, "skryte": False},
        {"nazov": "Banán", "cena": 0.39, "skryte": False},
        {"nazov": "Aviváž", "cena": 5.99, "skryte": False},
    ]
    max_cena = request.GET.get("max")
    if max_cena != "" and max_cena is not None:
        for item in data:
            if item["cena"] > float(max_cena):
                item["skryte"] = True
            else:
                item["skryte"] = False
    return render(request, "cv1/cv1_obchod.html", {"data": data})

def cv1_body(request):
    vysledok = None
    percenta = None
    body = None
    max_bodov = None
    
    if request.method == "POST":
        body = round(float(request.POST["body"]), 2)
        max_bodov = round(float(request.POST["max"]), 2)
        if max_bodov != 0 and body <= max_bodov:
            percenta = (body / max_bodov) * 100
            if(percenta >= 90):
                vysledok = 1
            elif(percenta >= 75):
                vysledok = 2
            elif(percenta >= 50):
                vysledok = 3
            elif(percenta >= 30):
                vysledok = 4
            else:
                vysledok = 5
        else:
            vysledok = "Chyba"
    return render(request, "cv1/cv1_body.html", {"vysledok": vysledok, "percenta": percenta, "body": body, "max_bodov": max_bodov})
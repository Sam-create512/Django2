from django.shortcuts import render

def index(request):
    text = "Toto je moja stranka s domacimi ulohami."
    return render(request, "domace/index.html", {"text": text})

def du2_vizitka(request):
    data = {
        "meno": "Samuel",
        "trieda": "3.AT",
        "vek": 17,
        "zaluby": ["Prax", "Programovanie", "3D Technologie"]
    }
    return render(request, "domace/du2_vizitka.html", data)
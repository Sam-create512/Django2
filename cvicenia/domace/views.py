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

def du3_teplota(request):
    teplota = None
    if request.method == "POST":
        teplotaIn = float(request.POST["teplotaIn"])
        if request.POST["jednotka"] == "C":
            teplota = round((teplotaIn - 32) * 5 / 9, 1)
        else:
            teplota = round(teplotaIn * 9 / 5 + 32, 1)

        jednotka = request.POST["jednotka"]

    return render(request, "domace/du3_teplota.html", {"teplota": teplota, "jednotka": jednotka})
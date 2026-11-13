from django.shortcuts import render, HttpResponse
import datetime

def ahoj(request):
    return HttpResponse("Ahoj Svet!")

def o_mne(request):
    kontext = {
        "meno": "Samuel",
        "vek": 17,
        "zaluby": ["hokej","matematika"]
    }
    return render(request, "ulohy/o_mne.html", kontext)

def rozvrh(request):
    hodiny = [
        {"cislo": 1, "predmet": "Programovanie"},
        {"cislo": 2, "predmet": "Programovanie"},
        {"cislo": 3, "predmet": "Programovanie"},
        {"cislo": 4, "predmet": "Anglictina"},
        {"cislo": 5, "predmet": "Prax"},
        {"cislo": 6, "predmet": "Prax"},
    ]
    return render(request, "ulohy/rozvrh.html", {"den": "Pondelok", "hodiny": hodiny})

def pozdrav(request):
    meno = request.GET.get("meno", "") # .get() je metoda, ktora ziskava hodnotu z GET requestu. Ak parameter "meno" nie je v requeste, vrati sa prazdny string.
    return render(request, "ulohy/pozdrav.html", {"meno": meno})

def sucet(request):
    vysledok = None
    if request.method == "POST":
        cislo1 = float(request.POST["cislo1"])
        cislo2 = float(request.POST["cislo2"])
        vysledok = cislo1 + cislo2

    return render(request, "ulohy/sucet.html", {"vysledok": vysledok})

def kalkulacka(request):
    vysledok = None
    if request.method == "POST":
        cislo1 = float(request.POST["cislo1"])
        cislo2 = float(request.POST["cislo2"])
        operacia = request.POST["operacia"]
        if operacia == "+":
            vysledok = cislo1 + cislo2
        elif operacia == "-":
            vysledok = cislo1 - cislo2
        elif operacia == "*":
            vysledok = cislo1 * cislo2
        elif operacia == "/":
            if cislo2 != 0:
                vysledok = cislo1 / cislo2
            else:
                vysledok = "Chyba: Delenie nulou nie je povolené."

    return render(request, "ulohy/kalkulacka.html", {"vysledok": vysledok})

def obdlznik(request):
    obsah, obvod = None, None
    if request.method == "POST":
        dlzka = float(request.POST["dlzka"])
        sirka = float(request.POST["sirka"])
        obsah = round(dlzka * sirka, 2)
        obvod = round(2 * (dlzka + sirka), 2)
    return render(request, "ulohy/obdlznik.html", {"obsah": obsah, "obvod": obvod})

def vek(request):
    vek = None
    if request.method == "POST":
        rok_narodenia = int(request.POST["rok_narodenia"])

        dnes = datetime.date.today()
        vek = dnes.year - rok_narodenia
    return render(request, "ulohy/vek.html", {"vek": vek})
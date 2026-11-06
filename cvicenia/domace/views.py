from django.shortcuts import render

def index(request):
    text = "Toto je moja stranka s domacimi ulohami."
    return render(request, "domace/index.html", {"text": text})
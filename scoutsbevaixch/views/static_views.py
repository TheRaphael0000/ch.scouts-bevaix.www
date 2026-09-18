from django.shortcuts import render


def accueil(request):
    return render(request, "accueil.html")


def scoutisme(request):
    return render(request, "scoutisme.html")


def actualites(request):
    return render(request, "actualites.html")


def calendrier(request):
    return render(request, "calendrier.html")


def emplacement(request):
    return render(request, "emplacement.html")


def locations(request):
    return render(request, "locations.html")
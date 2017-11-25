from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def noticias(request):
    return render(request, "noticias.html")



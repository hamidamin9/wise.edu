from django.shortcuts import redirect,render

def index(request):
    return render(request, "index.html")

def our_alumni(request):
    return render(request, "our_alumni.html")
from django.shortcuts import redirect,render

def index(request):
    return render(request, "index.html")

def our_alumni(request):
    return render(request, "our_alumni.html")

def about_us(request):
    return render(request, "about_us.html")

def ceo_message(request):
    return render(request, "ceo_message.html")

def goverment_collaboration(request):
    return render(request, "goverment_collaboration.html")

def our_team(request):
    return render(request, "our_team.html")

def executive_board(request):
    return render(request, "board_of_advisors.html")
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

def ongoing_projects(request):
    return render(request, "ongoing_projects.html")

def up_coming_projects(request):
    return render(request, "up_coming_projects.html")

def Earning_center_btn(request):
    return render(request, "Earning_center_btn.html")

def life_at_college(request):
    return render(request, "life_at_college.html")

def media(request):
    return render(request, "media.html")

def loan(request):
    return render(request, "loan.html")

def events(request):
    return render(request, "events.html")

def skill_institute(request):
    return render(request, "skill_institute.html")

def college_students(request):
    return render(request, "college_students.html")

def register(request):
    return render(request, "register.html")

# def wise_history(request):
#     return render(request, "wise_history.html")


def education_unemployed(request):
    return render(request, "education_unemployed.html")
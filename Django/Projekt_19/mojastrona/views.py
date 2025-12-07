from django.http import HttpResponse

def info_view(request):
    return HttpResponse("<h1>Informacje o stronie</h1>")    #  dodałem do task 1 lesson 20

def rules_view(request):
    return HttpResponse("<h1>Regulamin strony</h1>")    #  dodałem do task 1 lesson 20

def user_profile_view(request, username):
    return HttpResponse(f"<h1>Witaj na profilu, {username}!</h1>")   #  dodałem do task 2 lesson 20

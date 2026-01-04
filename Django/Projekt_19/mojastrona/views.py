from django.http import HttpResponse
from django.contrib.auth.decorators import login_required     #   dodaję w ramach task 3 lesson 24
from django.shortcuts import render    #   dodaję w ramach task 3 lesson 24

def info_view(request):
    return HttpResponse("<h1>Informacje o stronie</h1>")    #  dodałem do task 1 lesson 20

def rules_view(request):
    return HttpResponse("<h1>Regulamin strony</h1>")    #  dodałem do task 1 lesson 20

def user_profile_view(request, username):
    return HttpResponse(f"<h1>Witaj na profilu, {username}!</h1>")   #  dodałem do task 2 lesson 20

def about_view(request):
    return HttpResponse("<h2>To jest strona o nas (ABOUT)</h2>")   #  dodałem w ramach task 5 lesson 20

#   dodaję w ramach task 3 lesson 24:
@login_required
def profile(request):
    return render(request, 'users/profile.html')

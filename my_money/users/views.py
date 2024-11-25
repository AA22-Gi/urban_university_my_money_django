from django.shortcuts import render

def home(request):
    return render(request, 'users_html/home.html')

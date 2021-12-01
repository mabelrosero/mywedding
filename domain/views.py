from django.shortcuts import render

def index(request):
    return render(request,  'index.html',  {'name': 'Patricia', 'lastname': 'Rosero'})

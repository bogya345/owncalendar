from django.shortcuts import render

# Create your views here.

def index(request):
    data = {"active": "profile"}
    return render(request, 'profileapp/index.html', context = data)
from django.shortcuts import render

# Create your views here.

def index(request):
    data = {"active": "diary"}
    return render(request, 'diaryapp/index.html', context=data)
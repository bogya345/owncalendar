from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, logout

from django.contrib.auth.models import User


from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=100),
    password = forms.CharField(label="password", max_length=100)
class RegisterForm(forms.Form):
    username = forms.CharField(label="username", max_length=100),
    password = forms.CharField(label="password", max_length=100),
    email = forms.CharField(label="email", max_length=100),
    sex = forms.CharField(label="sex", max_length=100)

    # def __init__(self, username, password, email, sex):
        
        
    def forceInit(self, username, password, email, sex):
        self.username = username
        self.password = password
        self.email = email
        self.sex = sex
        return self

    def is_valid(self):
        if(self.username != '' and self.password != '' and self.email != '' and self.sex != ''):
            return True
        else:
            return False


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('/profile/')
    else:
        form = LoginForm()
        return render(request, 'authapp/index.html', { 'form': form } )

def register(request):
    if request.method == 'POST':
        form = RegisterForm()
        form.forceInit(request.POST['username'],request.POST['password'],request.POST['email'],request.POST['sex'])

        if form.is_valid():
            user = User.objects.create_user(form.username, form.email, form.password)
            user.save()
            form = LoginForm()
            return render(request, 'authapp/index.html', { 'form': form } )
        else:
            print('NOT VALID')

    form = RegisterForm()
    return render(request, 'authapp/registration.html', { 'form': form } )

def mainview(request):
    if request.user.is_authenticated:
        data = request.user
        return render(request, 'profileapp/index.html', context=data)
    else:
        form = LoginForm()
        return render(request, 'authapp/mainview.html', { 'form': form } )

def registrationview(request):
    if request.user.is_authenticated:
        data = request.user
        return render(request, 'profileapp/index.html', context=data)
    else:
        return render(request, 'authapp/registration.html', context=data)

def login(request):
    if request.user.is_authenticated:
        data = request.user
        return render(request, 'profileapp/index.html', context=data)
    else:
        user = authenticate(username='bogya', password='password')
        # if request.GET['username'] == "username" and request.GET['password'] == "password":
        if user is not None:
            data = {'user':request.user}
            return render(request, 'profileapp/index.html', context=data)
        else:
            return "Incorrect login and password"

def logoutUser(request):
    if request.user.is_authenticated:
        # close session
        logout(request)
        return render(request, 'authapp/mainview.html')
    else:
        return render(request, 'authapp/mainview.html')
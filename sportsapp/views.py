from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'sportsapp/index.html')

def register(request):
    if request.method == "POST":
        #username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Profile successfully created!!!")

        return redirect('login')

    return render(request, 'sportsapp/register.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'sportsapp/home.html', {'fname': fname})
        else:
            messages.error(request, "Check credentials and try again later!")
            return redirect('home')

    return render(request, 'sportsapp/login.html')

def signout(request):
    logout(request)
    messages.success(request, "You have successfully logged out!!")
    return redirect('home')

def homepage(request):
    return render(request, 'sportsapp/home.html')
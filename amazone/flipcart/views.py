from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect ('hello_world')
        else:
            error_message = "Invalid username or password."  # Add an error message if authentication fails
            return render(request, "flipcart/invalid.html", {'error_message': error_message})

    return render(request, "flipcart/signin.html")
@login_required(login_url="/signin")
def hello_world(request):
    return render(request, "flipcart/hello.html")

def signout(request):
    logout(request)
    messages.success(request, "logout successfully")
    return render(request, "flipcart/signin.html")

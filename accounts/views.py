from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .form import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    # future -> ?next=/articles/create/
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)

@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")

@login_required
def logout_view(request):    
    logout(request)
    return redirect("/")
    
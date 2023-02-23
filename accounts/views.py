from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .form import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save()                   
            username = form.cleaned_data.get('username')            
            raw_password = form.cleaned_data.get('password') 
            user.set_password(raw_password)
            user.save()             
            user = authenticate(username=username, password=raw_password)            
            login(request, user)
            return redirect('/')
        else:
            print('form invalid')
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})



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

def profile_view(request):
    pass

@login_required
def logout_view(request):    
    logout(request)
    return redirect("/")
    
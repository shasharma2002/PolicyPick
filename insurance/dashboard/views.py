from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def dashboard(request):
    return render(request,'registration/dashboard.html')

def about(request):
    return render(request, 'registration/about.html')

def comparison(request):
    return render(request, 'registration/comparer.html')

def logreg(request):
    return HttpResponse('this is login/register page')

def healthins(request):
    return render(request, 'healthins.html')

def autoins(request):
    return render(request, 'autoins.html')

def lifeins(request):
    return render(request, 'lifeins.html')

def healthdetail(request):
    return render(request, 'healthdetail.html')

def autodetail(request):
    return render(request, 'autodetail.html')

def lifedetail(request):
    return render(request, 'lifedetail.html')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def about_view(request):
    return render(request, 'registration/about.html')

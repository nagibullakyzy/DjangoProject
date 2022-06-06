from django.utils import timezone
from .models import Food,User
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .forms import UserForm
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def index(request):
    foods = Food.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    users = User.objects.all()
    return render(request, 'main/index.html', {'foods': foods,'users': users})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})





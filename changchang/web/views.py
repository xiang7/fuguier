from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.shortcuts import redirect

#login_required: redirects to settings.LOGIN_URL if not logged in

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def work(request):
    return render(request, 'work.html')

@login_required
def about(request):
    return render(request, 'about.html')
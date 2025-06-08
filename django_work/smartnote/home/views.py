from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home/index.html',{'date_': datetime.today()})  # passing the parameter

@login_required(login_url='/admin')
def login(request):
    return render(request, 'home/authorized_page.html',{})
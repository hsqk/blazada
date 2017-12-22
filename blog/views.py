from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Trackee
from .forms import TrackeeForm
import re, math


import requests
import bs4

# Create your views here.


def trackee_new(request):
    if request.method == 'POST':
        form = TrackeeForm(request.POST)
        if form.is_valid():
            #check mobile number
            #if new mobile number, prompt for password, scrape name, save in database, redirect to 
            #scrape name
            #save in database
            trackee = form.save(commit=False)
            response = requests.get(trackee.url)
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            trackee.name = str(soup.find("h1", { "class" : "product-info-name" } ))
            trackee.save()
            
            return redirect('trackee_new')
    else:
        form = TrackeeForm()
    return render(request, 'blog/trackee_new.html', {'form': form})

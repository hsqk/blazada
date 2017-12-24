from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Trackee, Tracker
from .forms import TrackeeForm
import re, math


import requests
import bs4

# Create your views here.


def trackee_new(request):
    if request.method == 'POST':
        form = TrackeeForm(request.POST)
        if form.is_valid():
            try:
                trackee = form.save(commit=False)
                response = requests.get(trackee.url)
                soup = bs4.BeautifulSoup(response.text, "html.parser")
                trackee.name = str.strip(soup.find("h1", { "class" : "product-info-name" } ).getText())
                tracker, created = Tracker.objects.get_or_create(mobile=trackee.mobile)
                trackee.tracker = tracker
                trackee.save()
                clearedForm = TrackeeForm(initial={'mobile':trackee.mobile})
                return render(request, 'blog/trackee_new.html', {'form': clearedForm, 'success': True, 'itemName': trackee.name, 'target': form.cleaned_data['target'], 'mobile':  trackee.mobile })
            except:
                return render(request, 'blog/trackee_new.html', {'form': form, 'success': False, })
    else:
        form = TrackeeForm()
    return render(request, 'blog/trackee_new.html', {'form': form, 'success': 0})

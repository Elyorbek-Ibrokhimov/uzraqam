# myapp/views.py

from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')


# myapp/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'myapp/dashboard.html')

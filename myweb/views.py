from django.shortcuts import render

# Create your views here.
def myweb_view(request):
    return render(request, 'myweb/home.html')

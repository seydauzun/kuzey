from django.shortcuts import render

# Create your views here.
def index(request):
    contex = dict()
    return render(request, 'home/index.html', contex)


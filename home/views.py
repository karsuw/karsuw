from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    text = "</br>Mrb Wrdsl </br> ihsan"
    context = {'text': text}

    return render(request, 'home/index.html', context)

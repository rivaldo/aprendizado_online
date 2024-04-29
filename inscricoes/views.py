from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inscricoes(request):
    return render(request, 'inscricoes/index.html')
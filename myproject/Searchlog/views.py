from django.shortcuts import render
from django.http import HttpResponse

def Searchlog(request):
    return render(request,"index.html")
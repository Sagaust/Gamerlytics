from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gamerlytical(request):
    return HttpResponse('Welcome to the Dashboard!')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
from .models import *
def startech(request):

    data = Startech.objects.all()
    # print(type(data))
    return HttpResponse(data)


def ryans(request):

    data = Ryans.objects.all()
    # print(type(data))
    return HttpResponse(data)



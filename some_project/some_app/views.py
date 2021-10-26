from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse('The pretty homepage c:')

from django.shortcuts import render
from django.http import HttpResponse


def get_new(request):
    return HttpResponse("Django alive")

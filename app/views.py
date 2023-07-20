from django.shortcuts import render

from django.http import HttpResponse

def surjana(request):
    return HttpResponse('<marquee><h1>hello how are you</h1></marquee>')

def rohan(request):
    return HttpResponse('<marquee><h1>rohan is not comming to calss</h1></marquee>')
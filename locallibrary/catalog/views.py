from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    '''
        return hello world string
    '''
    return HttpResponse('hello world')

from django.shortcuts import render
from django.http import HttpRequest,JsonResponse

# Create your views here.

def homePage(request:HttpRequest):
    response={"message": "Hello World!"}
    return JsonResponse(data=response)

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'PUT', 'DELETE'])
def hello_world(request):
    print(request)
    return JsonResponse({"result": True})

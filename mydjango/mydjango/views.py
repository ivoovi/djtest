from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    # context = {}
    template = 'home.html'
    return render(request,template)
    # return JsonResponse('hello',safe=False)

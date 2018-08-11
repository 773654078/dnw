from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def testone(request):
    return render(request, "items/adddItems.html")
from django.shortcuts import render
import requests

# Create your views here.
def recipes(request):
    return render(request, 'recipes.html', {'data': ""})
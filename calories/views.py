from django.shortcuts import render
import requests
import os
import json

names = []
values = []

# Create your views here.
def calories(request):
    global names, values
    if request.method == 'POST':
        query = request.POST['query'].strip()
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
        api_response = requests.get(api_url + query, headers={'X-Api-Key': os.environ['API_KEY']})
        try:
            data = json.loads(api_response.content)['items']
            print(type(data))
            names = list(data[0].keys())
            values = list(data[0].values())
        except Exception as e:
            data = {'message':"There was an error", 'query': query}
        return render(request, 'calories.html', {'data': data})
    else:
        return render(request, 'calories.html', {'data': ""})
    

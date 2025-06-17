from django.shortcuts import render
import requests
import os
import json
from .utils import plot_data

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
            keys_names = list(data[0].keys())
            keys_values = list(data[0].values())
            names = keys_names[1:]  # Skip the first key which is 'name'
            values = keys_values[1:]  # Skip the first value which is the name of
            chart = plot_data(names, values)
        except Exception as e:
            data = {'message':"There was an error", 'query': query}
        return render(request, 'calories.html', {'data': data, 'chart': chart})
    else:
        return render(request, 'calories.html', {'data': ""})
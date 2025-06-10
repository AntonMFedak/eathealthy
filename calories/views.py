from django.shortcuts import render
import requests
import os
import json

# Create your views here.
def calories(request):
    if request.method == 'POST':
        query = request.POST['query'].strip()
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
        api_response = requests.get(api_url + query, headers={'X-Api-Key': os.environ['API_KEY']})
        try:
            data = json.loads(api_response.content)['items']
            print(data)
        except Exception as e:
            data = "There was an error"
            print(e)
        return render(request, 'calories.html', {'data': data})
    else:
        return render(request, 'calories.html', {'data': ""})
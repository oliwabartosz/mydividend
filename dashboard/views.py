from django.shortcuts import render

import requests
import json

with open ('config.json') as config_file:
    config = json.load(config_file)

# Create your views here.
def home(request):

    if request.method == 'POST':
        ticker = request.POST.get('ticker')
        api_request = requests.get(f"{config['API_LINK']}{ticker}{config['API_KEY']}")

        try:
            api_data = json.loads(api_request.content)
        except Exception as e:
            api_data = False
            
        return render(request, 'home.html', {'api_data': api_data,})
    else:
        return render(request, 'home.html')
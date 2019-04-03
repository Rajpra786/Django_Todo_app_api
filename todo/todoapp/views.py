from django.shortcuts import render

# Create your views here.
import requests
import json

def home(request):

    response = requests.get('http://127.0.0.1:8000/api/task/tasks/?format=json')
    data = response.json()
    task =[];
    date =[];
    description=[];
    Id=[];
    for i in data:
        task.append(i['task_title'])
        date.append(i['date'])
        description.append(i['description'])

    data = zip(task,date,description)
    return render(request, 'home.html', {
        'data':data
    })

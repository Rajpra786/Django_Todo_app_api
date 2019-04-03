from django.shortcuts import render
# from django.http import JsonResponse
from . models import Task
from rest_framework import viewsets
from . import serializers

# def task_list(request):
#     result = []
#
#     for  i in Task.objects.all():
#         result.append({ 'name': i.task_title, 'Date': i.date , 'Description':i.description})
#
#     return JsonResponse(result,safe=False)



class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()

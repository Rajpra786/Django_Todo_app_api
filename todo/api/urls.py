from django.urls import path
from django.urls import include
# from . import views
#
# urlpatterns = [
#     path('task_list', views.task_list),
# ]
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('tasks', views.TaskViewSet)

urlpatterns = [
    path('task/', include(router.urls))
]

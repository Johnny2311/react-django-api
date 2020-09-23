from django.urls import path
from . import views

urlpatterns = [
    path('api/workers', views.WorkerListCreate.as_view()),
]

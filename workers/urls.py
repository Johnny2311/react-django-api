from django.urls import path
from . import views

urlpatterns = [
    path('api/workers', views.WorkerList.as_view()),
    path('api/workers/<int:pk>', views.WorkerDetail.as_view()),
]

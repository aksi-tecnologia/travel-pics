from django.urls import path
from . import views

urlpatterns = [
    path('pics/', views.PicsView.as_view(), name='pics'),
]

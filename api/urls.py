from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data, name='get_data'),
    path('info', views.get_info, name='get_info'),
]
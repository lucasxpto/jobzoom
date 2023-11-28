from django.urls import path
from jobs.views import home

urlpatterns = [
    path('', home, name='home'),
]

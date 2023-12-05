from django.contrib.auth import views
from django.urls import path

from .views import registrar, login_view

app_name = 'usuarios'

urlpatterns = [
    path('registrar/', registrar, name='registrar'),
    path('login/', login_view, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]

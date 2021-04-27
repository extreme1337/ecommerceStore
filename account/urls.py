from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.account_registration, name='register'),
    #path('activate/<slug:uid64>/<slug:token>)/', views.account_activate, name='activate'),
]

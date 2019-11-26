# Postlist/urls.py
from django.urls import path
from .views import list_and_create_view


urlpatterns = [
#    path('add/', PostCreateView.as_view(), name='add'), # new
    path('', list_and_create_view, name='home'),

]
